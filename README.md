# QuizCraft - AI Powered QuizGenerator

QuizGenerator is a Streamlit-based Python app that generates multiple-choice quizzes (MCQs) automatically from any text you provide. It uses a generative AI model (Google Gemini via the `google.generativeai` package) to create semantically relevant questions and presents them in an interactive web UI.

## What is this project?

- A small Streamlit application (`quizapp.py`) that converts input text into a short MCQ quiz.
- Useful for educators, students, or content creators who want quick assessment items from documents, articles, or notes.
- Generates questions using an AI model (Gemini) so the questions are based on the given content and follow the requested difficulty level.

## How it works

1. You paste or enter a piece of text into the app.
2. You choose a difficulty level (`Easy`, `Medium`, `Hard`).
3. When you click "Generate Quiz", the app sends a prompt (with the text and level) to the Google Generative AI model (Gemini).
4. The model responds with JSON-formatted MCQs (question text, options, and the correct option).
5. The app parses the response, displays each question with radio-button options, and waits for your answers.
6. After you submit, the app compares selected answers to the correct ones and shows your score and per-question feedback.

The core logic lives in `fetch_questions()` in `quizapp.py`: it formats a prompt, calls `genai.GenerativeModel.generate_content()`, cleans and parses the JSON response, and returns a list of MCQs for the UI to render.

## Features

- AI-generated MCQs from any supplied text
- Streamlit interactive UI for quizzes and scoring
- Configurable difficulty level
- Simple JSON response parsing so you can adapt question formats

## Requirements

- Python 3.8+ (the repo includes an optional `quiz_env` virtual environment)
- `pip` available on your PATH
- A Google Cloud API key with access to Gemini (set in `GOOGLE_API_KEY` in `.env`)

Required Python packages include `streamlit` and `google-generativeai`; use `requirements.txt` to install them.

## Installation

1. Clone the repository or copy the files to your machine.
2. (Recommended) Create and activate a virtual environment:

```powershell
python -m venv quiz_env
# Windows PowerShell
.\quiz_env\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file at the project root and set the required environment variable:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

Run the app with Streamlit:

```bash
streamlit run quizapp.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`) and use the UI to paste text, select level, generate the quiz, and submit answers.

## Development

- Use the included `quiz_env` virtual environment or create a new one as shown above.
- Edit `quizapp.py` to customize prompt templates, question count, or UI layout.

## Testing

There are no automated tests included by default. To add tests, create a `tests/` folder and use `pytest`:

```bash
pip install pytest
pytest
```

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-change`.
3. Make changes and add tests where appropriate.
4. Commit and push, then open a pull request.

## License

This project is provided under the MIT License by default. Replace with your preferred license if desired.

## Contact

If you need help or want to discuss features, open an issue or contact the project owner.
