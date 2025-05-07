from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials (Security Hotspot)
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def home():
    return render_template_string('''
        <h2>Login</h2>
        <form action="/login" method="POST">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pw = request.form['password']

    # No input sanitization or encryption (Vulnerability)
    if user == USERNAME and pw == PASSWORD:
        return render_template_string(contact_page_html())
    else:
        return "Invalid credentials"

def contact_page_html():
    return '''
        <h2>Contact Us</h2>
        <form action="/submit_contact" method="POST">
            Name: <input name="name"><br>
            Email: <input name="email"><br>
            Message:<br>
            <textarea name="message"></textarea><br>
            <input type="submit">
        </form>
    '''

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    msg = request.form['message']

    # Directly printing sensitive data (Code Smell)
    print(f"Name: {name}, Email: {email}, Message: {msg}")

    # No validation (Bug)
    return "Thanks for contacting us!"

if __name__ == "__main__":
    app.run(debug=True)
