from flask import Flask, render_template, request, session, redirect, url_for
import uuid

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Dictionary to store messages
messages = {}

# Home page route
@app.route('/')
def home():
    if 'user_id' not in session:
        # Generate a unique pseudonymous identifier for the user
        session['user_id'] = str(uuid.uuid4())
    return render_template('index.html', user_id=session['user_id'], messages=messages)

# Post message route
@app.route('/post_message', methods=['POST'])
def post_message():
    if 'user_id' in session:
        user_id = session['user_id']
        message = request.form['message']
        messages.setdefault(user_id, []).append(message)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
