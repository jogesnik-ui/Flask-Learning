# School Organiser — AI-Powered Task Manager

A web application that helps students manage assignments and get AI-powered study recommendations.

## Live Demo
[school-organiser.onrender.com](https://school-organiser.onrender.com)

## What It Does
- Add, complete, and delete school assignments
- View all tasks in a clean table with status badges
- Get AI-powered study recommendations — one click sends your pending tasks to Gemini and returns a prioritisation and study strategy

## Built With
- Python & Flask — web framework
- SQLite — database
- Google Gemini API — AI recommendations
- HTML & CSS — frontend
- Deployed on Render

## How It Works
Tasks are stored in a SQLite database. When you click "Get Study Recommendation", pending tasks are sent to the Gemini API which analyses deadlines and workload to recommend which task to prioritise and how to approach it.

## What I Learned
- Built with no tutorial — designed the architecture myself
- Flask routing, Jinja2 templating, SQLite database management
- API integration with conversation memory
- Full deployment pipeline from local development to live URL
- How to use claude code for styling and basic prompting

  Overall, this projects has deepend my understanding in multiple fields of coding which will be transfered into future projects. Obviously this was much more challenging then making a simple task organiser in the command line but it was a very fun and rewarding project!

## Setup
```bash
git clone https://github.com/jogesnik-ui/flask-organiser
cd flask-organiser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Add your Gemini API key to a `.env` file:
```
GEMINI_API_KEY=your_key_here
```
Then run:
```bash
python3 app.py
```
