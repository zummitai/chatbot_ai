import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from qa import prepare_data,answer_question
import datetime
import time

# loading environment variables
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define root domain to crawl
domain = "www.axamansard.com"
full_url = "https://www.axamansard.com/faqs/"


df=prepare_data(full_url,domain)

# uvicorn main:app --reload
# python -m uvicorn main:app --reload
# uvicorn main:app for production

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/answer")
def answer(question: str):
    return {"answer":answer_question(df,question=question,debug=False)}

# print(answer("Can we start a policy without visiting the office"))

# print(answer("what is axamansard insurance life insurance plan?"))

print(answer("i miss paying my premium for 2 years what are the consequences?"))
