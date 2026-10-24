🤝 FairMatch AI | Autonomous Talent & Career Mediator

Empowering Tier-1 Engineers & High-Growth Companies through Autonomous Matchmaking, Crustdata Graph Intelligence, and Direct Recruiter Automation.

FairMatch AI is a modern, two-sided autonomous talent mediation platform designed to solve bias, keyword-filtering gaps, and outreach friction in high-tier technical hiring (₹45L - ₹1Cr+ CTC). Powered by Gemini 3.8 Flash and Crustdata, FairMatch AI provides real-time job discovery, AI candidate-company fit evaluation, automated hiring manager discovery, and instant email dispatch.

🌟 Key Features

📊 Dual-Perspective Evaluation Engine: Generates parallel strategy dossiers for both candidates and hiring managers to bypass automated resume filters.

🔍 Live Tier-1 Job Discovery: Continuously monitors career opportunities at top engineering employers (Google, Stripe, Uber, Atlassian, Razorpay, etc.).

👥 Hiring Manager & Email Finder: Queries employee leadership graphs to discover and verify hiring decision-makers and corporate email patterns.

✉️ Automated Recruiter Outreach: Generates high-converting, personalized cold outreach emails with direct Gmail API / UI integration and local draft management.

⚡ Background Cron Job Monitor: Features an automated watchlist scanner that continuously monitors target companies and dispatches email digests when ideal matches are found.

🚀 Tech Stack

Frontend / UI: Streamlit with custom CSS (Enterprise Dark Mode styling)

AI / LLM Core: Gemini 3.8 Flash (google-generativeai)

Data & Intelligence: Crustdata Graph & Custom Evaluation Pipelines

Document Processing: pdfplumber (Resume parsing)

Email Delivery: Python smtplib / MIME Protocol & Direct Gmail Deep Linking

🛠️ Installation & Setup

Clone the Repository:

git clone https://github.com/your-repo/fairmatch-ai.git
cd fairmatch-ai


Install Dependencies:

pip install streamlit google-generativeai pdfplumber


Configure API Keys:
Update agent.py with your Gemini API key:

genai.configure(api_key="YOUR_GEMINI_API_KEY")


Launch the Application:

streamlit run app.py
