import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv()  # load all the environment from .env file

# from openai import OpenAI
import google.generativeai as genai
# client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@st.cache_data

def fetch_questions(text_content, quiz_level):

    RESPONSE_JSON = {
    "mcqs" : [
        {
            "mcq": "multiple choice question1",
            "options": {
                "a": "choice here1",
                "b": "choice here2",
                "c": "choice here3",
                "d": "choice here4"
            },
            "correct": "correct choice option"
        },
        {
            "mcq": "multiple choice question",
            "options": {
                "a": "choice here",
                "b": "choice here",
                "c": "choice here",
                "d": "choice here"
            },
            "correct": "correct choice option"
        },
        {
            "mcq": "multiple choice question",
            "options": {
                "a": "choice here",
                "b": "choice here",
                "c": "choice here",
                "d": "choice here"
            },
            "correct": "correct choice option"
        }
    ]
}
    
    PROMPT_TEMPLATE = """
    Text: {text_content}
    You are an expert in generating MCQ type quiz on the basis of provided content.
    Given the above text, create a quiz of 3 multiple choice questions keeping difficulty level as {quiz_level}
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Make sure to format your response like RESPONSE_JSON below and use it as a guide.
    Ensure to make an array of 3 MCQs referring the following response json.
    Here is the RESPONSE_JSON:
    
    {RESPONSE_JSON}
    
    """

    formatted_template = PROMPT_TEMPLATE.format(text_content=text_content, quiz_level=quiz_level, RESPONSE_JSON=RESPONSE_JSON)

    #Make API request
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(formatted_template)

    extracted_response = response.text

    print(extracted_response)

    import re

    cleaned_response = extracted_response.replace("```json", "").replace("```", "").strip()

    # remove trailing commas
    cleaned_response = re.sub(r',\s*([}\]])', r'\1', cleaned_response)

    print(cleaned_response)

    data = json.loads(cleaned_response)

    return data.get("mcqs", [])



def main():

    st.title("Quiz Generator App")

    # Text input for user to paste content
    text_content = st.text_area("Paste the text content here:")

    # Dropdown for selecting quiz level
    quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"])

    # Convert quiz level to lower casing
    quiz_level_lower = quiz_level.lower()

    #questions were getting diappeared so
    session_state = st.session_state

    #check if quiz_generated flag exists in session_state, if not initialize it to false
    if "quiz_generated" not in session_state:
        session_state.quiz_generated = False

    if not session_state.quiz_generated:
        session_state.quiz_generated = st.button("Generate Quiz")

    if session_state.quiz_generated:
        questions = fetch_questions(text_content=text_content, quiz_level=quiz_level_lower)

        # Display questions and radio buttons
        selected_options = []
        correct_answers = []
        for question in questions:
            options = list(question["options"].values())
            selected_option = st.radio(question["mcq"], options, index=None)
            selected_options.append(selected_option)
            correct_answers.append(question["options"][question["correct"]])

        # Submit button
        if st.button("Submit"):
            # Display selected options
            marks = 0
            st.header("Quiz Result:")
            for i, question in enumerate(questions):
                selected_option = selected_options[i]
                correct_option = correct_answers[i]
                st.subheader(f"{question['mcq']}")
                st.write(f"You selected: {selected_option}")
                st.write(f"Correct answer: {correct_option}")
                if selected_option == correct_option:
                    marks += 1
            st.subheader(f"You scored {marks} out of {len(questions)}")

if __name__ == "__main__":
    main()


