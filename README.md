# 🏛️ ONIX Council – Collaborative Intelligence Interface

ONIX Council is a local, interactive web application that allows you to ask a question not to a single language model, but to a **council of models** working together.

Instead of relying on one opinion, ONIX Council orchestrates multiple models to **deliberate, critique, refine, and finally agree** on a response—much like a panel of experts guided by a chairman.

The result is a more thoughtful, balanced, and well-reasoned answer.

---

## ✨ Core Idea

Most applications send a prompt to a single provider and return the first response.

ONIX Council takes a different approach:

* Multiple models receive the same question
* They iteratively review and refine a shared draft
* Each model must explicitly agree before consensus is reached
* A designated **Chairman** produces the final authoritative answer
* Individual member feedback is preserved for transparency

All of this happens live in a clean, ChatGPT-like interface.

---

## 🧠 How It Works

When you submit a query, the system follows these stages:

### Stage 1: Initial Deliberation

Each council member reviews the topic and contributes to a shared draft.
If a member is satisfied, they explicitly confirm it.
If not, they improve the draft.

This process repeats iteratively until consensus is reached or a maximum number of rounds is met.

---

### Stage 2: Consensus Check

The system ensures **all members are satisfied** with the draft.
Only when unanimous agreement is achieved does the process move forward.

This prevents premature or low-quality conclusions.

---

### Stage 3: Chairman’s Final Decision

Once consensus exists, the Chairman:

* Improves clarity
* Removes redundancy
* Produces a final, polished response

This answer is presented as the official outcome.

---

### Stage 4: Individual Final Feedback

Each council member provides:

* Agreement status
* One strength of the final answer
* One limitation or caveat (if any)

This preserves accountability and insight diversity.

---

## 🖥️ User Interface

The application uses a three-panel layout:

* **Left Panel** – Live deliberation stream
* **Center Panel** – Chairman’s final answer
* **Right Panel** – Individual member feedback

Previous questions are stored in session for quick reference.

---

## ⚙️ Installation

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

CHAIRMAN_NAME=Chairman
CHAIRMAN_MODEL=
CHAIRMAN_API_KEY=

MEMBER1_NAME=
MEMBER1_MODEL=
MEMBER1_API_KEY=
```

Make sure you have valid API credentials and sufficient usage credits.

---

### 3️⃣ Configure the Council (Optional)

Edit `config.py` to:

* Change the number of council members
* Assign different models to members
* Modify the chairman role

---

## ▶️ Running the Application

### Web Interface (Recommended)

```bash
streamlit run ui.py
```

### Terminal Mode (Optional)

```bash
python main.py
```

---

## 🛠️ Tech Stack

### Backend

* Python 3.9+
* Streamlit
* Requests
* Environment-based configuration

### Architecture

* Modular council logic
* Iterative consensus algorithm
* Stateless API calls
* Session-based UI state

### Storage

* In-memory session state (no database required)

---

## 🎯 Why This Project Matters

* Encourages multi-perspective reasoning
* Reduces single-model bias
* Makes agreement explicit
* Improves answer quality through iteration
* Designed for experimentation and extensibility

This project is ideal for research, exploration, and anyone interested in **collaborative intelligence systems**.

---

## 📌 Roadmap Ideas

* Persistent conversation storage
* Model performance analytics
* Visual voting or confidence scores
* Real-time token streaming
* Deployment support

---

## 📜 License

MIT License
© 2026 Pranil Shah
