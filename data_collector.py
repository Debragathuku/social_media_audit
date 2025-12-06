import pandas as pd

posts = [
    "These people should go back to where they came from!",
    "You are stupid and useless!",
    "Send money to claim your reward now!",
    "There will be a fight in town tonight.",
    "Have a nice day everyone!",
    "Join our investment group to double your money!",
    "You are such an idiot",
    "Let’s attack them now!",
    "Peace and unity for all.",
    "MPESA reward! Send 200 to receive 10,000!"
]

df = pd.DataFrame({"text": posts})
df.to_csv("tweets.csv", index=False)

print("Dummy tweets saved to tweets.csv")
