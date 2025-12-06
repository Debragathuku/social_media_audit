# Social Media Audit Prototype

This project is a prototype web app for auditing social media content, detecting:

- Hate speech
- Cyberbullying
- Violence
- Cyber fraud

## Live Demo

Access the dashboard using this public URL via ngrok:

[https://kinetic-shelba-translunar.ngrok-free.dev](https://kinetic-shelba-translunar.ngrok-free.dev)

> **Note:** The link works only while ngrok is running on the host machine.


## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run `python data_collector.py` to generate dummy tweets
3. Run `python classifier.py` to classify tweets
4. Run `python app.py` to start Flask server
5. Use ngrok: `ngrok.exe http 5000` to get a public URL

## Tech Stack

- Python 3.12
- Flask
- Pandas
- BeautifulSoup
- Transformers
