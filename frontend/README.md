# Artino Feedback App

A full-stack web application for collecting and analyzing feedback from customers and staff at Artino, designed to improve signage project quality and internal processes. The app features a Persian-language interface, built with React (frontend) and Flask (backend), and includes data analysis with Python.

## Features
- **Persian Feedback Form**: Users (customers or staff) submit feedback on signage projects or tasks via a modern, RTL interface.
- **Conditional Fields**: Customers select project types; staff select task processes.
- **Data Storage**: Feedback is saved to a CSV file (`بازخورد_۱۴۰۴.csv`) with UTF-8 encoding.
- **Analysis**: Python script (`analyze_feedback.py`) generates statistics and visualizations (issue frequency, satisfaction ratings) with proper Persian text rendering.
- **Deployment**: Frontend hosted on GitHub Pages (`https://M-for-Maniac.github.io/feedback-app`), backend on PythonAnywhere (`https://artinoco.pythonanywhere.com`).

## Tech Stack
- **Frontend**: React 18.3.1, Axios, CSS (with Vazir font for Persian)
- **Backend**: Flask 3.0.3, pandas 2.1.4, flask-cors, arabic_reshaper, python-bidi
- **Analysis**: pandas, matplotlib, arabic_reshaper, python-bidi
- **Hosting**: GitHub Pages (frontend), PythonAnywhere (backend)

## Setup (Local Development)
### Prerequisites
- Node.js 16+ (for frontend)
- Python 3.8+ (for backend)
- Git

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/M-for-Maniac/feedback-app.git
   cd feedback-app