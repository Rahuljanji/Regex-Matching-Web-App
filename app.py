from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def regex_results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex_pattern', '')

    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error:
        return "Invalid Regular Expression"

    # Redirect to a new page to display results
    return redirect(url_for('display_results', test_string=test_string, regex_pattern=regex_pattern, matches=matches))

@app.route('/display-results')
def display_results():
    test_string = request.args.get('test_string', '')
    regex_pattern = request.args.get('regex_pattern', '')
    matches = request.args.getlist('matches')

    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form.get('email', '')

    # Basic email validation regex
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        email_result = f"{email} is a Valid Email"
    else:
        email_result = f"{email} is an Invalid Email"

    return render_template('index.html', email_result=email_result)

# Main

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5000,debug=True)
