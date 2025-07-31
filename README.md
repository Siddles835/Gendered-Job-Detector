# Gendered Job Detector using GPT-2

**Overview**

Gendered Job Detector is a cutting-edge NLP application that analyzes job descriptions and flags implicit gender biases using a fine-tuned version of OpenAI's GPT-2 language model. 
The system identifies whether certain professions or role descriptions contain gendered language, allowing organizations and researchers to promote inclusivity and fairness in recruitment practices.
This project was developed in Python and uses Hugging Face's transformers library for model inference. 
It demonstrates a fusion of ethical AI development and deep learning—an ideal example of socially impactful AI.

**Features**

Uses GPT-2 to assess gender bias in job descriptions.
Supports batch processing of job listings.
Outputs a bias classification and explanation for each input.
Easily extendable for fine-tuning or integration with other bias detection tools.

Installation Guide
Follow these steps to get started:

**1. Clone the repository**
   
git clone https://github.com/yourusername/gendered-job-detector.git
cd gendered-job-detector

**2. Create a virtual environment (recommended)**
   
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
**OR**
venv\Scripts\activate     # Windows

**3. Install dependencies**
Make sure Python 3.8+ is installed.

pip install --upgrade pip
pip install -r requirements.txt

**How It Works**
You provide a sentence starter.
GPT-2 analyzes the word associations and contextual clues.
The system predicts what the description leans
Results are printed in Streamlit

**Explore the Bias**
This tool shows us the bias AI has when it comes to jobs. It's biased when it comes to both high and low valued jobs. Play around with it and look at the patterns with our model when it comes to gendered job bias.

**Ethical Considerations**
This tool aims to highlight and not reinforce gender bias. It's essential to treat this detector as an advisory system, not a decision-maker. We encourage ethical AI development practices and welcome feedback.

**Owner**

Sidhaanth Kapoor

Email: sidhaanthkapoor@gmail.com

GitHub: Siddles835

Interests: AI Ethics, ML, and CS
