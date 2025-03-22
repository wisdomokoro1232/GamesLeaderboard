from flask import Flask, render_template
from Queens import read_tracker

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    # Get the leaderboard data
    leaderboard = read_tracker()

    # Convert the DataFrame to a list of dictionaries
    players = leaderboard.to_dict(orient='records')

    # Pass the player data to the template
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)