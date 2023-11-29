
# nunc stack number back-calculator
# NSNBC
# MSNBC
# MSM
# COVID CONSPIRACY
# 5G :)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('5g.html')

app.run()
