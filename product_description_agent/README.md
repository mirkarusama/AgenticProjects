# Product Description Agent - LangChain Single Agent Project

A beginner-friendly project that teaches you how to build a **single agent** using **LangChain + OpenAI**. The agent takes raw product specs, a target customer, and a brand tone, and generates a persuasive, honest e-commerce listing.

## What You'll Learn

- How LangChain works (LLMs, prompts, tools, agents)
- How to create tools using the `@tool` decorator
- How an agent decides which tools to call and in what order
- How `PromptTemplate` shapes LLM output
- How the agent's tool-calling loop works (think -> act -> observe -> repeat)

## How It Works

```
Product specs, target customer, brand tone
       |
       v
  [Agent thinks: "I need to extract the product's value first"]
       |
       v
  [Tool: extract_product_value] --> builds a structured value map
       (features, benefits, differentiators, proof points, gaps)
       |
       v
  [Agent thinks: "Now I should write the listing"]
       |
       v
  [Tool: write_product_listing] --> title, summary, bullets, description, SEO meta
       |
       v
  Final product listing returned to user
```

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/mirkarusama/AgenticProjects
cd product_description_agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
.venv\Scripts\Activate
  ```
- **macOS / Linux:**
  ```bash
source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example env file and add your real key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Run

```bash
python product_description_agent.py
```

You'll see an interactive prompt:

```
PRODUCT DESCRIPTION AGENT (LangChain + OpenAI)
Describe the product: specs, target customer, and brand tone. Type 'quit' to exit.

Your product details:
```

Type your product details (e.g., `Specs: Stainless steel 1L insulated water bottle, keeps drinks cold for 24 hours...`) and the agent will generate a ready-to-publish listing. You'll also see a log line for each tool the agent calls.

## Example

**Input:**
```
Specs: Stainless steel 1L insulated water bottle, keeps drinks cold for 24 hours and hot for 12 hours, leak-proof lid, BPA-free, weighs 350g, available in 6 colors. Target customer: busy professionals and gym-goers. Brand tone: confident and energetic, no corporate jargon.
```

**Output:**
```
Title: Insulated Steel Water Bottle - 24Hr Cold, 12Hr Hot, Leak-Proof, 1L

Summary: Stay refreshed all day with a bottle built to keep pace with you -
cold for 24 hours, hot for 12, and never a drop out of place.

Benefit Bullets:
- 24-hour cold / 12-hour hot retention - one bottle for your coffee and your workout
- Leak-proof lid - toss it in your bag without worry
- BPA-free stainless steel - a safer daily-carry material
- 350g lightweight build - easy to carry all day
- 6 color options - match it to your style

Detailed Description:
Built for people who don't have time to babysit their water bottle, this
1L stainless steel bottle holds its temperature far longer than a typical
daily-carry option. The leak-proof lid means it goes straight into your gym
bag or backpack without a second thought...

SEO Meta Description: Insulated steel water bottle keeps drinks cold 24hrs,
hot 12hrs. Leak-proof, BPA-free, 350g. Available in 6 colors.
```

## Project Structure

```
.
├── product_description_agent.py   # Main agent code
├── requirements.txt                # Python dependencies
├── .env.example                    # API key template
├── .gitignore                      # Keeps secrets and venv out of git
└── README.md                       # This file
```

## Tech Stack

- [LangChain](https://python.langchain.com/) - Framework for building LLM applications
- [OpenAI GPT-4.1-mini](https://platform.openai.com/) - The LLM powering the agent
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management