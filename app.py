import random
from flask import Flask, redirect

app = Flask(__name__)
urls = ["https://nightcrawler.us", "http://alexb.io"]
number_range = 10000

@app.route('/')
def homepage():
    index = random.choice(range(number_range)) % 2
    url = urls[index]
    print(index)
    return redirect(url)

if __name__ == '__main__':
    app.run()
