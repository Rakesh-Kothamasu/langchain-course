import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello, LangChain!")
    print(os.environ.get("OPEN_AI_API_KEY"))
    print(os.environ.get("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
