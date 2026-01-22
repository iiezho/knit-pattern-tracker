# 🧶 Kint Pattern Tracker (MVP)

A lightweight pattern tracker for knitters and crocheters.

This project aims to help fiber artists follow patterns step by step, keep track of progress, and avoid losing their place in repetitive instructions.

The current version is an MVP built with Streamlit.

---

## 🤔 Why This Project

Following knitting or crochet patterns is surprisingly error-prone.

Many patterns involve:
- Repeating the same rows dozens of times
- Tracking progress across multiple sections
- Constantly switching between instructions and stitch references
- Losing count after interruptions

Existing solutions are often either:
- Paper-based (easy to lose your place)
- PDF readers with limited interactivity
- Feature-heavy apps that do not focus on step execution

This project explores a different approach:
**treating a pattern as a sequence of executable steps**, where progress, repetition, and state are explicitly tracked.

From a technical perspective, this project serves as:
- A product-focused experiment in workflow design
- A foundation for structuring semi-structured instructional text
- A platform for exploring pattern parsing, progress modeling, and user interaction data

---

## ✨ MVP Scope

The MVP focuses on one core problem:

> Helping users follow knitting or crochet patterns step by step without losing track of progress.

Currently supported features:
- Create a pattern by pasting text instructions
- Automatically split instructions into individual steps
- Step-by-step checklist to track progress
- Local sample pattern for testing and iteration

Features intentionally not included yet:
- Chart OCR or image parsing
- Hover-based stitch explanations
- Cloud sync or user accounts
- Automated or AI-based pattern parsing

---

## 🗂 Project Structure

stitch-pattern-tracker/
├── app/                  # Streamlit application
├── core/                 # Data models and storage logic
├── data/
│   └── sample_patterns/  # Example pattern text files
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

1. Clone the repository

git clone <your-repo-url>  
cd stitch-pattern-tracker

2. Create a virtual environment

python -m venv .venv  
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the app

streamlit run app/streamlit_app.py

---

## 🧪 Sample Pattern

A simple sample pattern is included in:

data/sample_patterns/sample1.txt

This file is used for early MVP testing and UI iteration.


