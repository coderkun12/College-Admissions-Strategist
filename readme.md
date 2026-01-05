# 🎓 College Admissions Strategist

### An Autonomous Multi-Agent AI System for Elite College Consulting

The **College Admissions Strategist** is an agentic AI framework built to revolutionize the university application process. By leveraging a swarm of specialized AI agents, the system provides personalized college shortlists, financial aid strategies, and deep-dive essay critiques that mimic high-end human admissions consulting.

---

## 🚀 Key Features

- **Personalized College Matchmaking:** Analyzes GPA, SAT/ACT, and extracurriculars to find "Reach," "Match," and "Safety" schools.
- **Financial Aid Optimization:** Strategizes for merit-based and need-based scholarships.
- **Essay Critique Engine:** High-level feedback on narrative flow, tone, and impact.
- **Multi-Agent Orchestration:** Uses a coordinated team of agents (Researcher, Strategist, and Editor) to ensure balanced advice.

## 🧠 Agent Architecture

This project utilizes a **Collaborative Agentic Loop**:

1.  **The Admissions Researcher:** Scrapes and analyzes current university data, rankings, and acceptance trends.
2.  **The Strategic Consultant:** Evaluates student profiles against historical admission benchmarks.
3.  **The Financial Advisor:** Specializes in FAFSA, CSS Profile navigation, and scholarship hunting.
4.  **The Chief Editor:** Refines the final output for tone and professional clarity.

## 🛠️ Tech Stack

- **Core Framework:** [CrewAI / LangChain] _(Specify your choice)_
- **LLM:** OpenAI GPT-4o / Claude 3.5 Sonnet
- **Memory:** Vector Embeddings for storing university data
- **Frontend:** [Streamlit / React] _(If applicable)_

## 📥 Getting Started

### Prerequisites

- Python 3.10+
- API Keys: OpenAI, Serper (for web search)

### Installation

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/coderkun12/College-Admissions-Strategist.git](https://github.com/coderkun12/College-Admissions-Strategist.git)
   cd College-Admissions-Strategist
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables: create a .env file:**
   `GROQ_API_KEY=your_key_here`
   `SERPER_API_KEY=your_key_here`
4. **Run the application:**
   ```bash
   python main.py
   ```

🤝 **Contributing**
Contributions are welcome! Please open an issue or submit a pull request for any feature enhancements.
