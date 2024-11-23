from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0,9)


@app.route("/game")
def home_page():
    return ("<h1 style='text-align: center;'>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif that count from 0-9'"
            "style='display: block; margin:0 auto;'>")

@app.route("/game/<int:guess>")
def guess_number(guess):
    if random_number < guess:
        return ("<h1 style='text-align: center;'>Too High!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='gif that count from 0-9'"
            "style='display: block; margin:0 auto;'>")
    elif random_number > guess:
        return ("<h1 style='text-align: center;'>Too Low!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='gif that count from 0-9'"
                "style='display: block; margin:0 auto;'>")
    elif random_number == guess:
        return ("<h1 style='text-align: center;'>Correct!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='gif that count from 0-9'"
                "style='display: block; margin:0 auto;'>")


if __name__ == "__name__":
    app.run(debug=True)
