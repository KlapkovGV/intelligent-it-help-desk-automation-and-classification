# intelligent-it-help-desk-automation-and-classification
This project aims to build a pipeline that automatically processes incoming messages to an IT department. The goal is to create a system that classifies requests by routing clear, script-readable information to a rule-based engine (Regex) and sending ambiguous cases to an LLM.

Initially, a classification system that processes messages seems quite straightforward in theory. We set up rules for regex, it collects messages based on keywords, and then messages that were not processed need to be passed to an LLM. It seems very simple, but during implementation, additional questions arise. 

Before getting start, let me outline the input data and requirements here.

Input Data: Connection problem, Hardware request, Access error, Access request, I'am getting an error message, Mail group addition, Report request, System error, Server unreachable, Application not working, VPN connection problem, VPN access request, Software installation, New user request, Permission request. 

An Excel sheet containing 3,000 email questions. These are example user messages from an IT help desk, providing a realistic dataset for testing the classification system.

The system is designed with 3 key stages:

Stage 1: Pre-Classification with Regex

In this stage, incoming IT department requests are processed by a python script using Regular Expressions. The script splits messages into two primary categories "ERROR" and "REQUEST". Classification is based on keyword matching, messages containing "problem", "error", "not working", "unreachable", "issue" are tagged as ERROR; those with "request", "addition", "installation" are tagged as REQUEST.

Stage 2: Hybrid Workflow Design

For this stage, I need to create and explain a logical workflow deagram. The diagram must imclude:
- Data input — incoming messages to the IT departmant
- Regex processing — messages are first classified as ERROR or REQUEST
- Routing to AI model — cases that cannot be processed by regex are sent to an Artificial Intelligence model for futher classification
- Final category assignment — after both regex and AI processing, each message is labeled with its final category

Stage 3: LLM Prompt Engineering
