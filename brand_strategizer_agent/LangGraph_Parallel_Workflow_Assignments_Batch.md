# LangGraph Parallel-Workflow Assignment

## Overview

You have been given a working LangGraph project — **Mental Wellness Practice Suggester** — as your reference implementation. Your task is to build your own unique use case using the same framework and graph pattern.

Study `mental_wellness_graph.py` carefully. Your graph must follow a similar structure:

```text
[User Input] -> [Understand / Classify Input]
                     |
                     +-> [Specialist Node 1] --+
                     +-> [Specialist Node 2] --+-> [Decision Node] -> [Conditional Final Output]
                     +-> [Specialist Node 3] --+
```

Each student below has been assigned a unique project. Build only the graph assigned to your name. Do not swap or copy another student's use case.

---

## What You Must Build

Use the same LangGraph patterns as the reference code:

- `StateGraph` to create the graph
- A Pydantic state model to define data fields
- Node functions where each node performs one clear job
- At least three parallel specialist nodes
- One decision node that reads all specialist outputs
- One conditional routing function
- At least two possible final-output nodes
- `ChatOpenAI` for LLM-based reasoning
- A `run_<your_project>()` function as the main entry point

Your graph must not copy the mental-wellness use case. Use the same architectural pattern to build your assigned project.

---

## Submission Steps

1. Fork or clone the reference repository.
2. Create your own Python file, such as `project_risk_graph.py`.
3. Do not modify `mental_wellness_graph.py`.
4. Build your assigned use case using the required LangGraph structure.
5. Test it end-to-end with your OpenAI API key.
6. Push your code to a new public GitHub repository under your own account.
7. Share the GitHub repository link in the Excel sheet shared on WhatsApp.

Your repository must contain:

- Your LangGraph `.py` file
- `requirements.txt`
- `.env.example`
- `.gitignore`
- `README.md` explaining the graph, routing logic, setup, and execution

Never commit your real `.env` file or API key.

---

## Student List

| No. | Name | Email |
|---:|---|---|
| 1 | Nidhi Mittal | Nidhi.goyal78@gmail.com |
| 2 | Jitendra Kumar Saroj | jitendra.saroj007@gmail.com |
| 3 | Vivek Harle | Vivek.harle1@gmail.com |
| 4 | Aditya Venkata Satyanarayana Mokkapati | adityamokkapati@gmail.com |
| 5 | Radharapu Bharath Kumar | bharathradharapu.1989@gmail.com |
| 6 | Avinash Dupaguntla | avinashd1276@gmail.com |
| 7 | Kailas Kanade | kailasukanade@gmail.com |
| 8 | Raviraj Deshpande | deshpande.raviraj@gmail.com |
| 9 | Sheetal Deshpande | rdeshpande.sheetal@gmail.com |
| 10 | Vishal Kailas Kharade | vishalkharade02@gmail.com |
| 11 | Usama Mirkar | mirkarusamaa@gmail.com |
| 12 | Hariharan | hareharankrish@gmail.com |
| 13 | Harmeet Bedi | hsbedi06@gmail.com |
| 14 | Valathappan Sivaraman | Valathappan@gmail.com |
| 15 | Balaji Kumar | Balajitkumar2@gmail.com |
| 16 | Surendran Sundarababu | ganeshh.suren@gmail.com |
| 17 | Mohit Luthra | manmohitluthra@gmail.com |
| 18 | Shirish Suryakant Pathak | shirishpathak86@gmail.com |
| 19 | Bhanupriya | Banupriya.uipath@gmail.com |
| 20 | Jolly Shringi | jollyshringi.888@gmaill.com |

> **Check required:** Jolly Shringi's email is reproduced exactly as provided. Confirm whether `gmaill.com` should be `gmail.com` before using it.

---

## Individual Assignments

### 1. Nidhi Mittal — Project Risk Advisor Graph

**Email:** Nidhi.goyal78@gmail.com  
**Python file:** `project_risk_graph.py`

**Use Case:** A user provides a project plan. The graph evaluates delivery, technical, and stakeholder risks in parallel.

- **Specialist Node 1 — `analyze_delivery_risks`:** Review schedule, resources, dependencies, and delivery constraints.
- **Specialist Node 2 — `analyze_technical_risks`:** Review architecture, integration, security, and scalability concerns.
- **Specialist Node 3 — `analyze_stakeholder_risks`:** Review ownership, communication, approvals, and adoption risks.
- **Decision Node — `assess_project_risk_level`:** Combine all specialist outputs and classify the overall risk as controlled or critical.
- **Conditional Route:** Route using the value returned in `risk_level`.
- **Final Nodes:** `standard_risk_register` and `critical_recovery_plan`.

---

### 2. Jitendra Kumar Saroj — Customer Feedback Analyzer Graph

**Email:** jitendra.saroj007@gmail.com  
**Python file:** `customer_feedback_graph.py`

**Use Case:** A user pastes customer reviews or survey responses. The graph extracts sentiment, themes, and improvement opportunities.

- **Specialist Node 1 — `analyze_sentiment`:** Classify positive, neutral, and negative feedback with evidence.
- **Specialist Node 2 — `extract_feedback_themes`:** Group comments into recurring product or service themes.
- **Specialist Node 3 — `identify_customer_requests`:** Extract requested features, fixes, and support needs.
- **Decision Node — `assess_customer_health`:** Decide whether feedback indicates normal improvement needs or urgent customer risk.
- **Conditional Route:** Route using `customer_health`.
- **Final Nodes:** `improvement_summary` and `urgent_customer_action_plan`.

---

### 3. Vivek Harle — Application Architecture Reviewer Graph

**Email:** Vivek.harle1@gmail.com  
**Python file:** `architecture_review_graph.py`

**Use Case:** A user describes a software architecture. The graph reviews quality attributes in parallel and recommends next steps.

- **Specialist Node 1 — `review_scalability`:** Examine load, bottlenecks, state, and scaling strategy.
- **Specialist Node 2 — `review_security`:** Examine authentication, authorization, secrets, data, and trust boundaries.
- **Specialist Node 3 — `review_reliability`:** Examine failure modes, retries, observability, recovery, and availability.
- **Decision Node — `classify_architecture_readiness`:** Decide whether the design is production-ready or requires redesign.
- **Conditional Route:** Route using `architecture_readiness`.
- **Final Nodes:** `production_readiness_report` and `architecture_redesign_plan`.

---

### 4. Aditya Venkata Satyanarayana Mokkapati — API Design Reviewer Graph

**Email:** adityamokkapati@gmail.com  
**Python file:** `api_design_review_graph.py`

**Use Case:** A user provides an API specification. The graph reviews usability, security, and resilience concurrently.

- **Specialist Node 1 — `review_api_contract`:** Check resources, methods, schemas, naming, and status codes.
- **Specialist Node 2 — `review_api_security`:** Check authentication, authorization, validation, and sensitive-data handling.
- **Specialist Node 3 — `review_api_resilience`:** Check idempotency, pagination, rate limits, timeouts, and error design.
- **Decision Node — `classify_api_quality`:** Classify the API as acceptable or revision-required.
- **Conditional Route:** Route using `api_quality`.
- **Final Nodes:** `api_approval_report` and `api_revision_plan`.

---

### 5. Radharapu Bharath Kumar — Production Incident Analyzer Graph

**Email:** bharathradharapu.1989@gmail.com  
**Python file:** `production_incident_graph.py`

**Use Case:** A user provides symptoms and logs. The graph analyzes application, infrastructure, and dependency causes in parallel.

- **Specialist Node 1 — `analyze_application_failures`:** Inspect exceptions, recent code changes, and application behaviour.
- **Specialist Node 2 — `analyze_infrastructure_failures`:** Inspect capacity, network, compute, storage, and deployment signals.
- **Specialist Node 3 — `analyze_dependency_failures`:** Inspect database, API, queue, and third-party service risks.
- **Decision Node — `determine_incident_severity`:** Combine evidence and classify the incident as standard or critical.
- **Conditional Route:** Route using `incident_severity`.
- **Final Nodes:** `standard_incident_plan` and `critical_incident_plan`.

---

### 6. Avinash Dupaguntla — Database Performance Advisor Graph

**Email:** avinashd1276@gmail.com  
**Python file:** `database_performance_graph.py`

**Use Case:** A user supplies a slow-query description, SQL, or execution details. The graph investigates multiple performance dimensions.

- **Specialist Node 1 — `analyze_query_structure`:** Review joins, filters, aggregations, subqueries, and result volume.
- **Specialist Node 2 — `analyze_index_strategy`:** Identify useful, missing, redundant, or poorly targeted indexes.
- **Specialist Node 3 — `analyze_database_load`:** Review locks, concurrency, memory, I/O, and workload conditions.
- **Decision Node — `classify_performance_issue`:** Decide whether optimization is straightforward or requires deep investigation.
- **Conditional Route:** Route using `performance_complexity`.
- **Final Nodes:** `quick_optimization_plan` and `deep_performance_investigation`.

---

### 7. Kailas Kanade — Course Recommendation Graph

**Email:** kailasukanade@gmail.com  
**Python file:** `course_recommendation_graph.py`

**Use Case:** A learner describes a goal and background. The graph evaluates skill gaps, learning style, and time constraints concurrently.

- **Specialist Node 1 — `assess_skill_gaps`:** Identify prerequisites, current strengths, and missing capabilities.
- **Specialist Node 2 — `assess_learning_preferences`:** Interpret preferred formats, pace, and practice style.
- **Specialist Node 3 — `assess_time_and_budget`:** Review schedule, deadline, and budget constraints.
- **Decision Node — `select_learning_intensity`:** Decide whether the learner needs a flexible or intensive path.
- **Conditional Route:** Route using `learning_intensity`.
- **Final Nodes:** `flexible_learning_path` and `intensive_learning_bootcamp`.

---

### 8. Raviraj Deshpande — Support Ticket Router Graph

**Email:** deshpande.raviraj@gmail.com  
**Python file:** `support_ticket_router_graph.py`

**Use Case:** A user submits a support issue. The graph evaluates intent, sentiment, and technical impact in parallel.

- **Specialist Node 1 — `classify_ticket_intent`:** Determine the product area and type of request.
- **Specialist Node 2 — `analyze_customer_sentiment`:** Detect frustration, urgency, and escalation signals.
- **Specialist Node 3 — `estimate_technical_impact`:** Assess affected users, blocked functions, and possible severity.
- **Decision Node — `choose_support_route`:** Decide whether the ticket follows standard support or escalation handling.
- **Conditional Route:** Route using `support_route`.
- **Final Nodes:** `standard_support_response` and `escalated_support_response`.

---

### 9. Sheetal Deshpande — Household Budget Health Graph

**Email:** rdeshpande.sheetal@gmail.com  
**Python file:** `budget_health_graph.py`

**Use Case:** A user provides household income, expenses, debts, and goals. The graph evaluates financial health from three angles.

- **Specialist Node 1 — `analyze_cash_flow`:** Compare income, essential costs, discretionary spending, and monthly surplus.
- **Specialist Node 2 — `analyze_debt_pressure`:** Review debt payments, interest burden, and repayment risks.
- **Specialist Node 3 — `analyze_savings_readiness`:** Review emergency savings and goal feasibility.
- **Decision Node — `classify_budget_health`:** Decide whether the budget is stable or needs corrective action.
- **Conditional Route:** Route using `budget_health`.
- **Final Nodes:** `stable_budget_plan` and `budget_recovery_plan`.

> Keep the output educational and clearly state that it is not professional financial advice.

---

### 10. Vishal Kailas Kharade — Candidate Evaluation Graph

**Email:** vishalkharade02@gmail.com  
**Python file:** `candidate_evaluation_graph.py`

**Use Case:** A user provides a resume and job description. The graph independently evaluates skills, experience, and communication evidence.

- **Specialist Node 1 — `evaluate_technical_skills`:** Compare required and demonstrated skills.
- **Specialist Node 2 — `evaluate_experience_fit`:** Compare responsibilities, seniority, domain, and outcomes.
- **Specialist Node 3 — `evaluate_profile_clarity`:** Review resume clarity, evidence, and measurable impact.
- **Decision Node — `classify_candidate_fit`:** Decide whether the candidate is a potential fit or requires substantial preparation.
- **Conditional Route:** Route using `candidate_fit`.
- **Final Nodes:** `interview_preparation_pack` and `candidate_gap_plan`.

---

### 11. Usama Mirkar — Brand Launch Strategist Graph

**Email:** mirkarusamaa@gmail.com  
**Python file:** `brand_launch_graph.py`

**Use Case:** A user describes a new product. The graph develops audience, positioning, and channel strategies in parallel.

- **Specialist Node 1 — `define_target_audience`:** Identify likely customer segments, needs, and objections.
- **Specialist Node 2 — `develop_brand_positioning`:** Create value proposition, differentiation, and messaging pillars.
- **Specialist Node 3 — `recommend_launch_channels`:** Compare suitable content, community, partnership, and paid channels.
- **Decision Node — `select_launch_strategy`:** Decide whether the launch should be focused or broad.
- **Conditional Route:** Route using `launch_strategy`.
- **Final Nodes:** `focused_launch_plan` and `multi_channel_launch_plan`.

---

### 12. Hariharan — Log Investigation Graph

**Email:** hareharankrish@gmail.com  
**Python file:** `log_investigation_graph.py`

**Use Case:** A user provides logs and system context. The graph investigates code, configuration, and environment causes concurrently.

- **Specialist Node 1 — `inspect_code_errors`:** Extract exceptions, failing functions, and code-related clues.
- **Specialist Node 2 — `inspect_configuration_errors`:** Inspect missing values, invalid settings, credentials, and version mismatches.
- **Specialist Node 3 — `inspect_environment_errors`:** Inspect runtime, capacity, connectivity, and external-service clues.
- **Decision Node — `classify_debugging_complexity`:** Decide whether the issue supports a direct fix or needs deeper diagnostics.
- **Conditional Route:** Route using `debugging_complexity`.
- **Final Nodes:** `direct_fix_checklist` and `deep_diagnostic_plan`.

---

### 13. Harmeet Bedi — Destination Planning Graph

**Email:** hsbedi06@gmail.com  
**Python file:** `destination_planning_graph.py`

**Use Case:** A user provides destination, duration, preferences, and budget. The graph plans attractions, food, and logistics in parallel.

- **Specialist Node 1 — `plan_attractions`:** Suggest sightseeing and experiences matching the user profile.
- **Specialist Node 2 — `plan_food_and_culture`:** Suggest local food and cultural activities.
- **Specialist Node 3 — `plan_trip_logistics`:** Consider geographic grouping, transport, pacing, and budget.
- **Decision Node — `select_itinerary_style`:** Decide whether the itinerary should be relaxed or activity-heavy.
- **Conditional Route:** Route using `itinerary_style`.
- **Final Nodes:** `relaxed_itinerary` and `activity_packed_itinerary`.

> Do not claim live pricing, opening hours, or availability unless the application retrieves current data.

---

### 14. Valathappan Sivaraman — Healthy Habit Planner Graph

**Email:** Valathappan@gmail.com  
**Python file:** `healthy_habit_graph.py`

**Use Case:** A user describes a lifestyle goal. The graph evaluates movement, nutrition habits, and recovery routines independently.

- **Specialist Node 1 — `review_movement_habits`:** Review general activity patterns and realistic movement opportunities.
- **Specialist Node 2 — `review_eating_habits`:** Review meal consistency, hydration, and stated dietary preferences.
- **Specialist Node 3 — `review_recovery_habits`:** Review sleep, breaks, stress routines, and schedule constraints.
- **Decision Node — `classify_change_readiness`:** Decide whether the user needs a gentle starter plan or structured habit plan.
- **Conditional Route:** Route using `change_readiness`.
- **Final Nodes:** `gentle_habit_starter` and `structured_habit_program`.

> Keep recommendations general and direct users to qualified professionals for medical or dietary conditions.

---

### 15. Balaji Kumar — Marketing Campaign Evaluator Graph

**Email:** Balajitkumar2@gmail.com  
**Python file:** `marketing_campaign_graph.py`

**Use Case:** A user describes a marketing campaign. The graph evaluates message, audience, and channel strategy in parallel.

- **Specialist Node 1 — `evaluate_campaign_message`:** Review clarity, value proposition, credibility, and call to action.
- **Specialist Node 2 — `evaluate_audience_fit`:** Review audience pain points, intent, objections, and segmentation.
- **Specialist Node 3 — `evaluate_channel_fit`:** Review suitability for email, social, search, events, or partnerships.
- **Decision Node — `classify_campaign_readiness`:** Decide whether the campaign is launch-ready or needs revision.
- **Conditional Route:** Route using `campaign_readiness`.
- **Final Nodes:** `campaign_launch_plan` and `campaign_revision_plan`.

---

### 16. Surendran Sundarababu — Software Requirements Quality Graph

**Email:** ganeshh.suren@gmail.com  
**Python file:** `requirements_quality_graph.py`

**Use Case:** A user provides draft requirements. The graph checks completeness, testability, and feasibility concurrently.

- **Specialist Node 1 — `check_requirement_completeness`:** Identify missing actors, flows, inputs, outputs, and exceptions.
- **Specialist Node 2 — `check_requirement_testability`:** Identify ambiguity and determine whether outcomes are measurable.
- **Specialist Node 3 — `check_requirement_feasibility`:** Review dependencies, constraints, risks, and assumptions.
- **Decision Node — `classify_requirement_quality`:** Decide whether requirements are sprint-ready or need clarification.
- **Conditional Route:** Route using `requirement_quality`.
- **Final Nodes:** `sprint_ready_specification` and `clarification_question_pack`.

---

### 17. Mohit Luthra — Dataset Quality Assessment Graph

**Email:** manmohitluthra@gmail.com  
**Python file:** `dataset_quality_graph.py`

**Use Case:** A user provides a dataset sample or profile. The graph evaluates completeness, consistency, and usability in parallel.

- **Specialist Node 1 — `assess_data_completeness`:** Analyze missing values, sparse fields, and record coverage.
- **Specialist Node 2 — `assess_data_consistency`:** Analyze formats, types, categories, duplicates, and conflicting values.
- **Specialist Node 3 — `assess_data_usability`:** Analyze relevance, bias indicators, sensitive fields, and fitness for purpose.
- **Decision Node — `classify_dataset_quality`:** Decide whether the dataset is usable or requires remediation.
- **Conditional Route:** Route using `dataset_quality`.
- **Final Nodes:** `data_usage_report` and `data_remediation_plan`.

---

### 18. Shirish Suryakant Pathak — Vendor Selection Graph

**Email:** shirishpathak86@gmail.com  
**Python file:** `vendor_selection_graph.py`

**Use Case:** A user provides vendor proposals. The graph compares capability, commercial value, and risk in parallel.

- **Specialist Node 1 — `compare_vendor_capabilities`:** Evaluate requirements coverage, expertise, integration, and support.
- **Specialist Node 2 — `compare_vendor_commercials`:** Evaluate transparent cost, value, contract terms, and hidden assumptions.
- **Specialist Node 3 — `compare_vendor_risks`:** Evaluate security, compliance, lock-in, delivery, and continuity risks.
- **Decision Node — `determine_vendor_outcome`:** Decide whether there is a clear recommendation or more due diligence is required.
- **Conditional Route:** Route using `vendor_outcome`.
- **Final Nodes:** `vendor_recommendation_report` and `vendor_due_diligence_plan`.

---

### 19. Bhanupriya — Learning Material Evaluator Graph

**Email:** Banupriya.uipath@gmail.com  
**Python file:** `learning_material_graph.py`

**Use Case:** A user provides learning content. The graph evaluates accuracy, clarity, and assessment readiness concurrently.

- **Specialist Node 1 — `evaluate_concept_coverage`:** Identify learning objectives, concepts, examples, and missing prerequisites.
- **Specialist Node 2 — `evaluate_explanation_clarity`:** Review structure, jargon, examples, and learner accessibility.
- **Specialist Node 3 — `evaluate_assessment_readiness`:** Determine whether the material supports meaningful practice questions.
- **Decision Node — `classify_material_readiness`:** Decide whether the material is learner-ready or requires improvement.
- **Conditional Route:** Route using `material_readiness`.
- **Final Nodes:** `learner_ready_study_pack` and `content_improvement_plan`.

---

### 20. Jolly Shringi — Event Planning Graph

**Email:** jollyshringi.888@gmaill.com  
**Python file:** `event_planning_graph.py`

**Use Case:** A user describes an event. The graph plans program, logistics, and guest experience in parallel.

- **Specialist Node 1 — `plan_event_program`:** Develop agenda, activities, timing, and host requirements.
- **Specialist Node 2 — `plan_event_logistics`:** Review venue, equipment, catering, staffing, transport, and contingency needs.
- **Specialist Node 3 — `plan_guest_experience`:** Review invitations, accessibility, communication, engagement, and feedback.
- **Decision Node — `classify_event_complexity`:** Decide whether the event needs a simple checklist or detailed execution plan.
- **Conditional Route:** Route using `event_complexity`.
- **Final Nodes:** `simple_event_checklist` and `detailed_event_execution_plan`.

---

## Evaluation Criteria

| Criteria | Points |
|---|---:|
| Code follows the same LangGraph structure as `mental_wellness_graph.py` | 20 |
| Uses Pydantic state, `StateGraph`, nodes, edges, and conditional routing correctly | 20 |
| Includes at least three parallel specialist nodes | 15 |
| Decision node reads all specialist outputs before routing | 15 |
| Graph runs end-to-end without errors | 10 |
| `README.md` clearly explains the use case and how to run it | 10 |
| GitHub repository is public, clean, and has `.env.example` without a real API key | 10 |
| **Total** | **100** |

---

## Tips

- Run `mental_wellness_graph.py` before building your own graph.
- Keep every node focused on one responsibility.
- Add one state field for every important specialist output and routing decision.
- Use fan-out and fan-in edges so all three specialist nodes run before the decision node.
- Use `messages: Annotated[list, operator.add]` if you want to track node logs.
- Make the decision node return a small structured value that the routing function can read reliably.
- Test both possible final routes.
- Include a Mermaid or simple flow diagram in your `README.md`.
- Do not push `.env`, `venv`, `.venv`, or `__pycache__` to GitHub.

---

*Deadline and submission link: shared on WhatsApp. Post your public GitHub repository URL in the Excel sheet.*
