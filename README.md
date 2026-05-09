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
.AI-based error analysis
.Root cause detection
.Suggested fixes
.Prevention guidance
.Simple terminal interface

## Tech Stack
.Python
.Groq API
.Llama 3 Model

## Installation
    pip install -r requirements.txt

## Run the Project
    python debug_copilot.py

## Example Input
    groq.GroqError: The api_key client option must be set

## Example Output
    Root Cause:
    The root cause of this error is that the `api_key` client option is not set in the Groq client configuration.

    Suggested Fix:
    Review the code where the Groq client is initialized to ensure that the `api_key` option is included in the client configuration. The Groq client is usually initialized using the `groq.client()` function.
    Replace `'YOUR_API_KEY_HERE'` with your actual Groq API key. You can obtain the API key from your Groq account or the Groq documentation.


## Key Learning

The project highlighted that the biggest challenge in debugging is often not finding solutions, but deciding the next best step when multiple possible causes exist.

AI becomes most useful when it reduces confusion and structures the debugging workflow.