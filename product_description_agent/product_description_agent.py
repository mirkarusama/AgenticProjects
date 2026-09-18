"""Product Description Agent — a LangChain agent that extracts a product's
real value from raw specs, then writes a persuasive, honest e-commerce listing.

Setup: pip install -r requirements.txt, copy .env.example to .env, add your key.
Run:   python product_description_agent.py
"""

import logging
import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("product_description_agent")

load_dotenv()
if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("sk-your"):
    logger.error("OPENAI_API_KEY not set. Copy .env.example to .env and add your key.")
    sys.exit(1)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

# ----------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------

EXTRACT_VALUE_PROMPT = PromptTemplate(
    input_variables=["specs", "target_customer", "brand_tone"],
    template="""You are an honest conversion copywriter's research assistant.

Given the raw product specifications below, separate the real, verifiable value
of this product. Do not invent capabilities that are not supported by the specs.

Product specifications: {specs}
Target customer: {target_customer}
Brand tone: {brand_tone}

Return a structured product value map with these sections:
- Features: factual attributes of the product, taken directly from the specs
- Benefits: what each feature means for the target customer, in their own terms
- Differentiators: what sets this product apart from typical alternatives, only if supported by the specs
- Proof points: concrete numbers, certifications, or claims from the specs that back up the benefits
- Missing information: anything a persuasive listing would normally need that isn't in the specs (flag it, don't fabricate it)

Return ONLY the value map, nothing else.""",
)

WRITE_LISTING_PROMPT = PromptTemplate(
    input_variables=["value_map"],
    template="""You are an expert e-commerce copywriter who never invents product
capabilities beyond what's supported by the value map below.

Product value map:
{value_map}

Using only what's in the value map, write a ready-to-publish product listing with:
- Title: a clear, keyword-rich product title (under 70 characters)
- Summary: a 1-2 sentence hook that leads with the strongest benefit
- Benefit bullets: 4-6 scannable bullets, each pairing a feature with its customer benefit
- Detailed description: 2-3 short paragraphs weaving in differentiators and proof points
- SEO meta description: under 160 characters, written to earn the click

If the value map flags missing information that would normally strengthen a section,
write around it honestly rather than inventing details.

Return ONLY the product listing, nothing else.""",
)


@tool
def extract_product_value(specs: str, target_customer: str, brand_tone: str) -> str:
    """Separate features, benefits, differentiators, proof points, and missing
    information from raw product specs. Use this FIRST."""
    logger.info("[extract_product_value] extracting value for: %s", specs[:80])
    return llm.invoke(
        EXTRACT_VALUE_PROMPT.format(
            specs=specs, target_customer=target_customer, brand_tone=brand_tone
        )
    ).content


@tool
def write_product_listing(value_map: str) -> str:
    """Turn a structured product value map into a ready-to-publish listing
    (title, summary, benefit bullets, description, SEO meta). Use AFTER
    extract_product_value."""
    logger.info("[write_product_listing] writing listing from value map")
    return llm.invoke(WRITE_LISTING_PROMPT.format(value_map=value_map)).content


# ----------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------

SYSTEM_PROMPT = """You are an honest conversion copywriter. Your job is to turn raw
product details into persuasive and accurate e-commerce copy.

When the user gives you product specifications (and, if available, the target
customer and brand tone), follow these steps:
1. First, use the extract_product_value tool to build a structured product value map.
2. Then, use the write_product_listing tool to turn that value map into a
   ready-to-publish listing.
3. Return the final listing to the user.

Always use both tools in order: extract first, then write. Never invent product
capabilities that aren't supported by the specs provided."""

agent = create_agent(
    model=llm, tools=[extract_product_value, write_product_listing], system_prompt=SYSTEM_PROMPT
)


def run_product_description_agent(product_details: str) -> str:
    """Run the agent on raw product details and return the finished listing."""
    result = agent.invoke({"messages": [HumanMessage(content=product_details)]})
    return result["messages"][-1].content


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main() -> None:
    print("\nPRODUCT DESCRIPTION AGENT (LangChain + OpenAI)")
    print("Describe the product: specs, target customer, and brand tone. Type 'quit' to exit.\n")

    while True:
        product_details = input("Your product details: ").strip()
        if not product_details:
            continue
        if product_details.lower() in ("quit", "exit", "q"):
            break

        try:
            listing = run_product_description_agent(product_details)
            print("\n" + "=" * 60)
            print(listing)
            print("=" * 60 + "\n")
        except Exception as e:
            logger.error("Agent failed: %s", e)


if __name__ == "__main__":
    main()
    