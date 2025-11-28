import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
from bs4 import BeautifulSoup
import requests

# Load environment variables from .env (for local dev)
load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_website_contents(url: str) -> str:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    # Limit to 2000 chars to avoid huge prompts
    return (title + "\n\n" + text)[:2000]

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")

system_prompt = """
You are a helpful assistant that summarizes the content of website into a concise summary and formatted way.
"""

user_prompt_prefix = """
These are the contents of the website, summarize the whole website including important links.
"""

# OpenAI-compatible client pointing to Gemini endpoint
client = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

def summarize(url: str) -> str:
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model="gemini-2.5-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_prefix + website}
        ]
    )
    return response.choices[0].message.content

# ---------- STREAMLIT UI ----------
st.title("🌐 AI Website Summarizer")
st.write("Paste any website URL and get a clean summary.")

url = st.text_input("Enter Website URL")

if st.button("Summarize"):
    if not google_api_key:
        st.error("GOOGLE_API_KEY is not set. Please configure it in your environment.")
    elif url:
        with st.spinner("Summarizing..."):
            try:
                summary = summarize(url)
                st.markdown(summary)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a valid URL.")
