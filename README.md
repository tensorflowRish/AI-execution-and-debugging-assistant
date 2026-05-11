## AI Execution & Debugging Assistant

## Overview

This project is a small Proof of Concept for an AI-assisted debugging workflow system.

The goal is to reduce debugging confusion by providing:

.root cause analysis
.step-by-step fix suggestions
.structured debugging guidance
.prevention recommendations

## Problem Statement

Developers often spend significant time switching between documentation, search engines, terminal logs, and AI tools while debugging.

This project explores how AI can help reduce decision fatigue and provide clearer execution flow during debugging sessions.

## Features
Semantic Memory (FAISS)
.Stores past errors as embeddings
.Retrieves similar issues using semantic similarity
.Enables learning from past debugging sessions
Rule Based Escalation Engine
.number of attempts
.similarity of past errors
.success/failure history
LLM Debugging Agent
Generates:
.root cause
.next steps
.prevention strategies
.Uses memory + escalation context
Persistent Storage
.FAISS index → vector memory
.JSON → metadata history (fixes, status, attempts)

## Project Structure
ai-debugging-assistant/
│
├── src/
│   ├── agents/
│   │   ├── debugger_agent.py        # LLM reasoning engine
│   │   ├── memory_agent.py          # memory + retrieval handler
│   │
│   ├── core/
│   │   ├── llm_client.py            # LLM API interface
│   │   ├── escalation_engine.py     # dynamic escalation logic
│   │   ├── formatter.py             # output formatting
│   │
│   ├── storage/
│   │   ├── memory.json              # metadata store
│   │   ├── index.faiss              # vector store
│   │
│   ├── main.py                      # system orchestrator
│
├── requirements.txt
├── .env
└── README.md

## Tech Stack
.Python
.FAISS (Vector Database)
.SentenceTransformers
.LLM API (Groq / OpenAI)
.NumPy

## Installation
    pip install -r requirements.txt

## Run the Project
    python main.py

## Example Input
    ModuleNotFoundError: No module named 'dotenv'

## Example Output
    ROOT CAUSE:
    The Python environment is missing the required package 'python-dotenv', which is needed to load environment variables.

    NEXT BEST STEP:
    Install the missing dependency using:
    pip install python-dotenv

    WHY THIS MAKES SENSE:
    The error indicates that Python cannot find the required module in the current environment, which typically happens when the package is not installed.

    PREVENTION:
    Ensure all project dependencies are listed in requirements.txt and installed inside a virtual environment.

## Test the Workflow
After running the main.py file:
    1. type the error...example - ModuleNotFoundError: No module named 'dotenv'
    2. enter attempted fix
    3. enter result (worked or failed)
Re-run the similar error:
    1. ModuleNotFoundError: No module named 'dotenv'
        You should see:
        higher attempt number
        similar past fixes retrieved
        escalation logic applied
This testing flow demonstrates:
 - Memory persistence

Errors are remembered across runs
 - Attempt tracking

System learns from repeated failures
 - Context-aware debugging

Similar errors influence reasoning
 - Escalation behavior

System changes strategy over retries

Expected System Behavior
    First run → direct fix suggestion
    Repeated failure → deeper diagnostic reasoning
    Similar past errors → memory-informed response
    New unrelated error → fresh analysis
## Key Learning

The project highlighted that the biggest challenge in debugging is often not finding solutions, but deciding the next best step when multiple possible causes exist.

AI becomes most useful when it reduces confusion and structures the debugging workflow.