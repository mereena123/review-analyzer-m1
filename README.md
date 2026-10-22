# Review Analyzer

A lightweight Python application for classifying product reviews and customer feedback.

## Purpose
Review Analyzer turns a free-text customer review into one of three labels:
`positive` (contains "good"), `negative` (contains "bad") or `unknown`.
Text is cleaned first: converted to lower case, trimmed, and runs of
spaces/tabs/newlines collapsed to a single space.

## Prerequisites
- Python 3.8 or newer
- Git

No third-party packages are required.

## Installation
```bash
git clone https://github.com/mereena123/review-analyzer-m1.git
cd review-analyzer-m1
python3 -m venv .venv            # optional
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

## Run
```bash
python3 app.py          # runs the demo
python3 test_app.py     # runs the tests (also works with: pytest)
```

## Example input / output
| Input                              | Output     |
|------------------------------------|------------|
| `"Good product"`                   | `positive` |
| `"  Really BAD packaging "`        | `negative` |
| `"Delivered yesterday"`            | `unknown`  |

```bash
$ python3 app.py
positive
```

## Project structure
```
review-analyzer-m1/
├── app.py          # normalize_review() and classify_review()
├── test_app.py     # assertions for normalisation and classification
├── README.md       # this file
└── .gitignore      # excludes caches, virtual envs and .env secrets
```
