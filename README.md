
```markdown
# Remote Healthcare & Emergency Response Portal - AI Chatbot Prototype
(This is done as part of my virtual internship by SWECHAAP.ORG)

An entirely local, private, and empathetic medical AI assistant prototype designed for a **Remote Health Care & Emergency Response Portal**. This chatbot runs completely offline on your local machine using **Ollama** and open-source Large Language Models (LLMs) like Meta's Llama 3. It requires **no API keys** and ensures total data privacy.

---

## 🚀 Features

- **100% Offline & Private:** Runs entirely on your local CPU/GPU hardware. No external data is sent to third-party cloud services.
- **Empathetic Response Engine:** Engineered using system context training to prioritize warmth, reassurance, and conversational engagement instead of sounding like a robotic script.
- **Actionable Home Precautions:** Provides clear, safe, and practical home remedies and precautions (e.g., hydration, rest, symptom monitoring) tailored to what the user feels.
- **Emergency Safeguard Trigger:** Continuously monitors conversation inputs for critical signs (e.g., severe chest pain, breathing difficulties) and instantly appends a `[TRIGGER_SOS]` system hook flag for the portal's ambulance tracking ecosystem.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Model Engine:** [Ollama](https://ollama.com)
- **Local LLM:** `llama3:8b` (Can also use lighter alternatives like `phi3` or `gemma2:2b`)
- **Python Library:** `ollama`

---

## 📦 Project Setup & Installation

### 1. Install Ollama
Download and install the background engine installer for your operating system from [ollama.com/download](https://ollama.com/download).

### 2. Download the Model
Open your Command Prompt or Terminal and pull the Llama 3 weights locally:
```bash
ollama run llama3:8b

```

*(Once the download completes, you can test it in the CLI, then type `/exit` to close the interactive session).*

### 3. Setup Python Environment

Install the official Ollama Python binding library:

```bash
pip install ollama

```

### 4. Run the Chatbot

Navigate to your project directory and execute the pure Python script:

```bash
python local_health_bot.py

```

---

## 🧠 Dynamic System Prompt "Training"

The chatbot's conversational behavior is shaped directly in the backend code using system instruction architecture. It enforces a strict operational protocol:

1. **Acknowledge with Empathy:** Address user discomfort before delivering facts.
2. **Educate Safely:** Decodes potential causes in simple, accessible language.
3. **Outline Precautions:** Formats clean bullet points outlining safe, comforting home care habits.
4. **AI Disclaimer:** Appends a mandatory medical disclaimer clarifying that it is an informational AI, not a human doctor.

---

## 🗺️ Future Dashboard Integration Strategy

This prototype maps directly into the **User Dashboard** layout of the broader portal wireframe. The conversational outputs can eventually be parsed by a web/mobile framework (like React or Flutter) to automatically transition users to features like **Book your Appointment**, **Blood Bank Information**, or trigger the **SOS Ambulance Tracker** overlay when a critical event flag is identified.

---
