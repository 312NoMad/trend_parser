<h1>HOW TO RUN PROJECT</h1>

1. Create a project repository
2. Create virtual environment and activate it
   1. python3 -m venv venv
   2. source venv/bin/activate
3. Download the remote repository
    1. git clone https://github.com/312NoMad/trend_parser.git
4. Install requirements
   1. pip install -r requirements.txt
5. Run project
   1. uvicorn main:app --reload
