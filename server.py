"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
                Enter <a href="/hello">'here'.</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    ### how to automate option values. Would concatenate string before with
        ### dropdown, and ending part of script.

    # dropdown = "<select ...=..>"
    # for comp in AWESOMENESS:
    #     dropdown += """<option value='{}'>{}</option>""".format(comp, comp)
    # drop+= '</select>'
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Select your compliment: <select name="compliment">
            <option value='awesome'>awesome</option>
            <option value='terrific'>terrific</option>
            <option value='fantastic'>fantastic</option>
            <option value='neato'>neato</option>
            <option value='wowza'>wowza</option>
            <option value='fantabulous'>fantabulous</option>
            <option value='oh-so-not-meh'>oh-so-not-meh</option>
            <option value='fantastic'>fantastic</option>
            <option value='brilliant'>brilliant</option>
            <option value='ducky'>ducky</option>
            <option value='coolio'>coolio</option>
            <option value='incredible'>incredible</option>
            <option value='wonderful'>wonderful</option>
            <option value='smashing'>smashing</option>
            <option value='lovely'>lovely</option>
            </select>
          <input type="submit" value="Submit">
        </form>
        <br/><br/><h1>OR!!!!!</h1><br/>
        <form action="/greet"><br/><br/>
        What's your name? <input type="text" name="person"><br/>
          Select your rude greeting: <br/>
          <input type="radio" name="compliment" value='asshole'>asshole</input><br/>
          <input type="radio" name="compliment" value='bumsicle'>bumsicle</input><br/>
          <input type="radio" name="compliment" value='boot-muncher'>boot-muncher</input><br/>
          <input type="radio" name="compliment" value='fairy-fart'>fairy fart</input><br/>
          <input type="radio" name="compliment" value='blanched-whale'>blanched whale</input><br/>
          <input type="submit" value="Submit">
        </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
