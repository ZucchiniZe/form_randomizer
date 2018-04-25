import random
from flask import Flask, redirect

app = Flask(__name__)
urls = [
        "https://docs.google.com/forms/d/e/1FAIpQLSfR9OndPPOYZc8r3EmwdoZkQocZJmicHesw3vfQ2g8XN-kCMQ/viewform?usp=sf_link", # control group
        "https://docs.google.com/forms/d/e/1FAIpQLScRQuExGj4OS51DO5I7K8qCqZqU46sqVq3UiFTmbw4KFfjABA/viewform?usp=sf_link", # blue group
        "https://docs.google.com/forms/d/e/1FAIpQLSedTEyb29zhNmuVYb2QXw5QgkyiEKhT4HS_-ymv84ODlAC7Bw/viewform?usp=sf_link", # red group
        "https://docs.google.com/forms/d/e/1FAIpQLScr4vEwJ0rCIA4DXQ92rMSztGK39BU62ZcXoAdNj-b-auqFjw/viewform?usp=sf_link"  # green group
        ]
number_range = 10000

@app.route('/')
def homepage():
    # get the index from a random number out of `number_range` numbers and then get
    # the modulo of the length of urls so we have an index that fits
    index = random.choice(range(number_range)) % len(urls)
    url = urls[index]

    print(f"Got {url}, redirecting")
    return redirect(url)

if __name__ == '__main__':
    app.run()
