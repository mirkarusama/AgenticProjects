# =============================================================================
# Product Launch Strategy Builder -- A LangGraph Learning Project
# =============================================================================
#
# This project teaches you how LangGraph works by building a product launch
# strategy assistant that develops audience, positioning, and channel plans.
#
# WHAT THIS DOES:
# A user describes a new product (e.g. "A subscription box for artisanal
# coffee beans", "An AI-powered budgeting app for freelancers"). The system
# runs 3 specialist nodes in PARALLEL (audience, positioning, channels), then
# a decision node picks the launch strategy and routes to either a FOCUSED
# launch plan (narrow, single-channel) or a MULTI-CHANNEL plan (broad,
# multi-channel) based on the product and market fit.
#
# LANGGRAPH CONCEPTS COVERED:
# 1. State Management (Pydantic) -- product description flows through the graph
# 2. Nodes -- each function does one job (audience, positioning, channels, etc.)
# 3. Parallel Execution -- 3 specialist nodes run at the same time
# 4. Fan-in -- waiting for all 3 specialist notes before deciding the strategy
# 5. Conditional Edges -- routing to focused vs broad based on the decision
# 6. Graph Compilation -- turning the graph definition into a runnable app
#
# GRAPH STRUCTURE:
#
#   START
#     |
#   understand_product
#     |
#     +---> define_target_audience -------+
#     |                                   |
#     +---> develop_brand_positioning ----+---> select_launch_strategy
#     |                                   |         |
#     +---> recommend_launch_channels ----+    (conditional)
#                                            /              \
#                                       focused?          broad?
#                                         |                  |
#                                focused_launch_plan   multi_channel_launch_plan
#                                         |                  |
#                                        END                END
#
# HOW TO RUN:
#   python launch_strategy_graph.py
#
# DEPENDENCIES (same as requirements.txt):
#   langgraph, langchain-openai, python-dotenv, pydantic
#
# =============================================================================

import sys
import operator
import json
from typing import Annotated

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()


class LaunchState(BaseModel):
    product_description: str = ""
    audience_notes: str = ""
    positioning_notes: str = ""
    channel_notes: str = ""
    needs_broad_launch: bool = False
    strategy_reason: str = ""
    final_plan: str = ""
    messages: Annotated[list, operator.add] = []


llm = ChatOpenAI(model="gpt-4.1-mini", temperature=1.5)


def understand_product(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are a sharp product launch strategist. "
        f"A user describes a new product: '{state.product_description}'. "
        f"Summarize what the product is and who it's roughly for in 1-2 sentences. "
        f"Then classify the launch complexity as SIMPLE, MODERATE, or COMPLEX in one word on a new line like: Complexity: SIMPLE"
    )
    return {
        "messages": [f"[understand_product] {response.content}"]
    }


def define_target_audience(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are a target audience research specialist. "
        f"The product is: '{state.product_description}'. "
        f"Identify the most likely customer segment(s), their core needs, and their "
        f"biggest objections to buying. "
        f"Keep it under 5 sentences."
    )
    return {
        "audience_notes": response.content,
        "messages": [f"[define_target_audience] Done"]
    }


def develop_brand_positioning(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are a brand positioning strategist. "
        f"The product is: '{state.product_description}'. "
        f"Create a value proposition, a key point of differentiation from "
        f"competitors, and 1-2 messaging pillars. "
        f"Keep it under 5 sentences."
    )
    return {
        "positioning_notes": response.content,
        "messages": [f"[develop_brand_positioning] Done"]
    }


def recommend_launch_channels(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are a go-to-market channel strategist. "
        f"The product is: '{state.product_description}'. "
        f"Compare suitable content, community, partnership, and paid channels, "
        f"and recommend which would work best for this launch. "
        f"Keep it under 5 sentences."
    )
    return {
        "channel_notes": response.content,
        "messages": [f"[recommend_launch_channels] Done"]
    }


def select_launch_strategy(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are a launch strategy decision system. The product is: '{state.product_description}'.\n\n"
        f"Here are three notes from specialists:\n\n"
        f"AUDIENCE:\n{state.audience_notes}\n\n"
        f"POSITIONING:\n{state.positioning_notes}\n\n"
        f"CHANNELS:\n{state.channel_notes}\n\n"
        f"Decide: should this launch be FOCUSED (narrow audience, one or two channels, "
        f"good for niche or early-stage products) or BROAD / MULTI-CHANNEL (wide audience, "
        f"several channels at once, good for mass-market or well-funded products)?\n\n"
        f"Reply STRICTLY in this JSON format (no other text):\n"
        f'{{"needs_broad_launch": true/false, "reason": "one sentence explanation"}}'
    )
    try:
        result = json.loads(response.content)
        needs_broad = result["needs_broad_launch"]
        reason = result["reason"]
    except (json.JSONDecodeError, KeyError):
        needs_broad = False
        reason = "Could not parse decision, defaulting to focused launch."

    return {
        "needs_broad_launch": needs_broad,
        "strategy_reason": reason,
        "messages": [f"[select_launch_strategy] broad_launch={needs_broad}"]
    }


def focused_launch_plan(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are a sharp, pragmatic launch consultant. The product is: '{state.product_description}'.\n\n"
        f"Based on these specialist notes, create a FOCUSED launch plan "
        f"(narrow audience, one or two channels) that combines the best elements:\n\n"
        f"AUDIENCE: {state.audience_notes}\n"
        f"POSITIONING: {state.positioning_notes}\n"
        f"CHANNELS: {state.channel_notes}\n\n"
        f"Format it as a simple numbered list of concrete action steps. "
        f"Keep it practical and easy to execute. End with a motivating closing line."
    )
    return {
        "final_plan": f"FOCUSED LAUNCH PLAN\n{'='*45}\n{response.content}",
        "messages": [f"[focused_launch_plan] Generated focused plan"]
    }


def multi_channel_launch_plan(state: LaunchState) -> dict:
    response = llm.invoke(
        f"You are an experienced go-to-market lead. The product is: '{state.product_description}'.\n\n"
        f"Based on these specialist notes, create a MULTI-CHANNEL launch plan "
        f"that thoughtfully combines all three approaches:\n\n"
        f"AUDIENCE: {state.audience_notes}\n"
        f"POSITIONING: {state.positioning_notes}\n"
        f"CHANNELS: {state.channel_notes}\n\n"
        f"Structure it in 3 phases: Prepare (audience & positioning alignment), "
        f"Launch (coordinated multi-channel push), Sustain (follow-through and momentum). "
        f"Give clear step-by-step actions for each phase with rough timing. "
        f"Keep it practical and motivating. End with a strong closing message."
    )
    return {
        "final_plan": f"MULTI-CHANNEL LAUNCH PLAN\n{'='*45}\n{response.content}",
        "messages": [f"[multi_channel_launch_plan] Generated multi-channel plan"]
    }


def route_after_decision(state: LaunchState) -> str:
    if state.needs_broad_launch:
        return "broad"
    else:
        return "focused"


graph = StateGraph(LaunchState)

graph.add_node("understand_product", understand_product)
graph.add_node("define_target_audience", define_target_audience)
graph.add_node("develop_brand_positioning", develop_brand_positioning)
graph.add_node("recommend_launch_channels", recommend_launch_channels)
graph.add_node("select_launch_strategy", select_launch_strategy)
graph.add_node("focused_launch_plan", focused_launch_plan)
graph.add_node("multi_channel_launch_plan", multi_channel_launch_plan)

graph.add_edge(START, "understand_product")

graph.add_edge("understand_product", "define_target_audience")
graph.add_edge("understand_product", "develop_brand_positioning")
graph.add_edge("understand_product", "recommend_launch_channels")

graph.add_edge("define_target_audience", "select_launch_strategy")
graph.add_edge("develop_brand_positioning", "select_launch_strategy")
graph.add_edge("recommend_launch_channels", "select_launch_strategy")

graph.add_conditional_edges(
    "select_launch_strategy",
    route_after_decision,
    {
        "focused": "focused_launch_plan",
        "broad": "multi_channel_launch_plan",
    }
)

graph.add_edge("focused_launch_plan", END)
graph.add_edge("multi_channel_launch_plan", END)

app = graph.compile()


def run_launch_strategy(product_description: str):
    print("=" * 55)
    print("  PRODUCT LAUNCH STRATEGY BUILDER")
    print(f"  Product: \"{product_description}\"")
    print("=" * 55)

    result = app.invoke({
        "product_description": product_description,
        "messages": [],
    })

    print("\n" + "=" * 55)
    print("  YOUR LAUNCH PLAN")
    print("=" * 55)
    print(f"\n{result['final_plan']}")

    print("\n" + "-" * 55)
    print("  MESSAGE LOG")
    print("-" * 55)
    for msg in result["messages"]:
        print(f"  {msg}")

    return result


if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  PRODUCT LAUNCH STRATEGY BUILDER")
    print("=" * 55)
    print("\n  Describe your new product and I'll build a")
    print("  personalized launch strategy just for you.")
    print("  Type 'quit' to exit.\n")

    while True:
        product_description = input("  Describe your product > ").strip()

        if product_description.lower() in ("quit", "exit", "q"):
            print("\n  Good luck with the launch. Goodbye!\n")
            break

        if not product_description:
            continue

        run_launch_strategy(product_description)
        print("\n")