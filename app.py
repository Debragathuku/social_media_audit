from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = pd.read_csv("classified_tweets.csv")

    total = len(df)
    hate = len(df[df["classification"] == "hate_speech"])
    cyber = len(df[df["classification"] == "cyberbullying"])
    fraud = len(df[df["classification"] == "fraud"])
    violence = len(df[df["classification"] == "violence"])
    clean = len(df[df["classification"] == "clean"])

    return render_template(
        "dashboard.html",
        total=total,
        hate=hate,
        cyber=cyber,
        fraud=fraud,
        violence=violence,
        clean=clean,
        table=df.to_html(classes="table table-bordered")
    )

if __name__ == "__main__":
    app.run(debug=True)
