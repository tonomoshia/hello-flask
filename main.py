from flask import Flask
from flask import request



app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form = """
<!doctype html>
<html>
    <body>
    <form>
        <label for="first_name">First Name</label>
        <input id="first_name" type="text" name="first_name" />
        <input type="submit" />
    </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

app.run()
