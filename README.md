# 🌐 AI Website Summarizer (Gemini + Streamlit)

A simple and powerful web application that uses **Google Gemini (via OpenAI-compatible API)** to summarize any website into a clean, concise, and well-formatted overview.

Just paste a URL and get an AI-generated summary including important content and links.

---

## 🖥️ Live Demo

https://websitesummariser.streamlit.app/

---

## 🚀 Features

* ✅ Summarizes any public website URL
* ✅ Cleans unwanted elements (scripts, images, forms, ads)
* ✅ AI-powered concise and formatted output
* ✅ Built with Streamlit for interactive UI
* ✅ Uses Google Gemini 2.5 Pro via OpenAI-compatible API

---

## 📂 Project Structure

```
ai-website-summarizer/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env   (local only, not pushed to GitHub)
```

---

## ⚙️ Prerequisites

Make sure you have:

* Python 3.9 or higher
* A Google Gemini API Key
  Get it from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## 🛠️ Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/vinay845/website_summariser_gemini_streamlit.git
cd ai-website-summarizer
```

---

### 2. Create a virtual environment

Using `venv`:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Or using `uv`:

```bash
uv venv
uv pip install -r requirements.txt
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

⚠️ Do not commit this file to GitHub. It is already ignored via `.gitignore`.

---

### 5. Run the application

Start the Streamlit server:

```bash
streamlit run app.py
```

Then open your browser and visit:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters a website URL.
2. The app fetches HTML using `requests`.
3. Content is cleaned using BeautifulSoup.
4. Clean text is sent to Gemini AI.
5. AI returns a concise, formatted summary.

---

## 🧰 Tech Stack

* Python
* Streamlit
* Google Gemini API
* BeautifulSoup
* Requests
* OpenAI SDK (compatible mode)

---

## 🛡️ Security Notes

* Never expose your API key publicly.
* Always use environment variables for secrets.
* `.env` file is excluded from Git tracking.

---

## 📌 Future Improvements

* Adjustable summary length
* Multi-language support
* Download summary as PDF
* Batch URL processing
* Dark mode UI

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit pull requests to improve the project.

---

## 📬 Contact

For questions or suggestions, open an issue in the repository.

---

### ⭐ If this project helped you, consider giving it a star!







