---
title: Know About Madiha
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
python_version: 3.11
app_file: app.py
pinned: false
---

# Know About Madiha — AI Portfolio Assistant

An AI-powered portfolio assistant built with **Python and Gradio** that allows users to interactively explore Madiha Shaikh’s professional profile.
The system uses **Clean Architecture principles** and integrates two models to provide both profile-based responses and general AI conversation.
https://huggingface.co/spaces/Madihaa/Know-About-Madiha.
---

## Overview

This project is a conversational AI interface designed to present **professional portfolio information in an interactive way**.
Instead of reading a static CV, users can ask questions about Madiha Shaikh’s:

* Background
* Skills and technologies
* Projects
* Work experience
* Education
* Contact information

The assistant responds using a structured **profile knowledge model** or a **general AI model**.

---

## Models Used

### 1. Madiha Info Model

A custom information model that answers questions specifically about **Madiha Shaikh's professional profile**.

Users can ask questions such as:

* Who is Madiha?
* Show Madiha’s skills
* What projects has Madiha worked on?
* What is Madiha’s experience?
* What technologies does Madiha use?
* How can I contact Madiha?

This model retrieves structured data from the profile configuration and generates targeted responses.

---

### 2. General AI Model (phi3 via Ollama)

The system also integrates a **general-purpose language model** using **phi3 through Ollama**.

This model allows users to ask:

* General AI questions
* Technology explanations
* Programming questions
* Open-ended conversations

Note:
The general model runs **locally through Ollama** and may not be available in cloud deployments.

---

## Architecture

The project follows a **Clean Architecture structure** to separate responsibilities and keep the system modular.

```
src
│
├── domain
│   └── chat_model.py
│
├── application
│   └── chat_router.py
│
└── infrastructure
    ├── config
    │   └── madiha_profile.py
    └── models
        ├── info_model.py
        └── general_model.py
```

### Layers

**Domain Layer**

* Defines the core chat model interface.

**Application Layer**

* Handles routing logic between models.

**Infrastructure Layer**

* Implements the actual models and configuration.

---

## Tech Stack

* Python
* Gradio
* Clean Architecture
* Ollama
* phi3 Language Model

---

## Installation

Clone the repository:

```
git clone https://github.com/Madihaa-Shaikh/Know-About-Madiha.git
cd Know-About-Madiha
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the chatbot:

```
python app.py
```

The interface will open in your browser.

---

## Example Questions

Try asking the assistant:

```
Who is Madiha?
Show Madiha's skills
Tell me about Madiha's projects
What technologies does Madiha use?
Give me a CV summary
```

---

## About Madiha

Madiha Shaikh is an **AI Engineer and Computer Vision enthusiast** pursuing a **Master’s degree in Artificial Intelligence at Brandenburg University of Technology (BTU), Germany**, expected to be completed in **April 2026**.

Her work focuses on:

* Computer Vision
* 3D Perception
* Depth Estimation
* RGB-D Data Processing
* Machine Learning Deployment
* Real-time AI systems

She has experience working on **industrial collaboration projects with PACE Aerospace Engineering, Fraunhofer, Siemens, Rolls-Royce, and BTU Germany.**

---

## Future Improvements

* Deploy a cloud-based LLM for the general chat model
* Add portfolio visualization (projects gallery)
* Add voice interface
* Add real-time model explanations

---

## License

This project is intended for **portfolio and demonstration purposes**.
