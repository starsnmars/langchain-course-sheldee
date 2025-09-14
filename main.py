import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenAI
load_dotenv()


def main():
    print("Hello from langchain-course!")
    # print("Your Google API Key is:", os.getenv("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
