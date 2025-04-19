from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the form data (e.g., save to database or send email)
    return redirect('/success')

@app.route('/success')
def success():
    return "Thank you for your message! We'll get back to you soon."

if __name__ == '__main__':
    app.run(debug=True)