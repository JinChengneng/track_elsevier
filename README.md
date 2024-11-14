# Track Elsevier

A web application to track peer review status in Elsevier's Author Hub. This tool allows authors to monitor the review progress of their manuscripts using the manuscript UUID.

## Features

- Track manuscript review status
- View basic manuscript information
- Monitor reviewer timeline and acceptance status
- Clean and responsive Bootstrap UI

## Local Development Setup

1. Clone the repository:

```bash
git clone https://github.com/JinChengneng/track_elsevier.git
cd track_elsevier
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
set FLASK_APP=app.py
flask run
```

4. Access the application at `http://127.0.0.1:5000/`.
