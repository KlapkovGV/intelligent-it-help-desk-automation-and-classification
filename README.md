# intelligent-it-help-desk-automation-and-classification
This project aims to build a pipeline that automatically processes incoming messages to an IT department. The goal is to create a system that classifies requests by routing clear, script-readable information to a rule-based engine (Regex) and sending ambiguous cases to an LLM.

Initially, a classification system that processes messages seems quite straightforward in theory. We set uo rules for regex, regex collects messages based on keywords, and then messages that were not precessed need to be passed to an LLM. It seems very simple, but during implementation, additional questions arise. 

Before getting start, let me outline the input data and requirements here.

Input Data: Connection problem, Hardware request, Access error, Access request, I'am getting an error message, Mail group addition, Report request, System error, Server unreachable, Application not working, VPN connection problem, VPN access request, Software installation, New user request, Permission request. 

An Excel sheet containing 3,000 email questions. These are example user messages from an IT help desk, providing a realistic dataset for testing the classification system.

The system is designed with 3 key stages:

Stage 1: Pre-Classification with Regex

Stage 2: Hybrid Workflow Design

Stage 3: LLM Prompt Engineering
