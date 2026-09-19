# Product Launch Strategy Builder - Learn LangGraph Step by Step

A beginner-friendly LangGraph project that develops a personalized product
launch strategy based on a short product description.

The project demonstrates a clear LangGraph pattern:

```text
[Product Description]
      |
      v
understand_product
      |
      +--> define_target_audience -----+
      +--> develop_brand_positioning ---+--> select_launch_strategy
      +--> recommend_launch_channels ---+          |
                                                conditional
                                             /              \
                                  focused_launch_plan   multi_channel_launch_plan
                                             |              |
                                            END            END
```

---

## What This Project Does

A user describes a new product such as:

- `A subscription box for artisanal coffee beans`
- `An AI-powered budgeting app for freelancers`
- `A new budget smartphone for emerging markets`

The graph then:

1. Understands the product and its rough audience.
2. Runs three specialist nodes in parallel:
   - target audience specialist
   - brand positioning specialist
   - launch channel specialist
3. Uses a decision node to choose whether the launch should be:
   - a focused launch (narrow audience, one or two channels), or
   - a broad, multi-channel launch
4. Routes to the correct final node.
5. Prints the personalized launch plan and message log.

---

## LangGraph Concepts Covered

| Concept | Where It Appears |
|---|---|
| State | `LaunchState` Pydantic model |
| Nodes | `understand_product`, `define_target_audience`, `develop_brand_positioning`, `recommend_launch_channels`, `select_launch_strategy`, `focused_launch_plan`, `multi_channel_launch_plan` |
| Parallel execution | Three specialist nodes run after `understand_product` |
| Fan-in | All three specialist notes flow into `select_launch_strategy` |
| Conditional edges | `route_after_decision` sends the graph to focused or broad launch |
| Final output | `focused_launch_plan` or `multi_channel_launch_plan` |
| Message accumulation | `messages: Annotated[list, operator.add]` |

---

## Project Files

```text
launch_strategy_graph.py   Main LangGraph project
architecture.md            Architecture explanation
architecture.drawio        Diagram source file
requirements.txt           Python dependencies
.env.example               Example environment file
.gitignore                 Ignored local files
```

---

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure your OpenAI API key

```powershell
copy .env.example .env
```

Edit `.env` and add your API key:

```text
OPENAI_API_KEY=sk-...
```

Never commit your real `.env` file.

### 4. Run the project

```powershell
python launch_strategy_graph.py
```

---

## Expected Flow

Example input:

```text
An AI-powered budgeting app for freelancers.
```

The graph will:

1. Summarize the product and its rough audience.
2. Identify the target audience, their needs, and objections.
3. Generate a brand positioning and messaging pillars.
4. Recommend suitable launch channels.
5. Decide whether the launch should be focused or multi-channel.
6. Print the final launch plan.
7. Print the message log showing which nodes executed.

---

## Code Walkthrough

| Step | What Happens | File |
|---|---|---|
| 1 | Define `LaunchState` | `launch_strategy_graph.py` |
| 2 | Initialize `ChatOpenAI` | `launch_strategy_graph.py` |
| 3 | Define graph node functions | `launch_strategy_graph.py` |
| 4 | Define `route_after_decision` | `launch_strategy_graph.py` |
| 5 | Add nodes and edges to `StateGraph` | `launch_strategy_graph.py` |
| 6 | Compile graph as `app` | `launch_strategy_graph.py` |
| 7 | Run with `run_launch_strategy()` | `launch_strategy_graph.py` |

---

## Important Note

This is a learning project, not a professional marketing or business strategy
tool. The output is meant for general brainstorming and educational purposes
only. For real launches, validate any strategy with market research and a
qualified marketing professional.

---

## Key Takeaways

1. State holds the data that travels through the graph.
2. Nodes are normal Python functions that read state and return updates.
3. Parallel execution happens when one node connects to multiple next nodes.
4. Fan-in happens when multiple nodes connect into one later node.
5. Conditional edges let the graph choose the next path at runtime.