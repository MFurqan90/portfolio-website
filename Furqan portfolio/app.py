from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import secrets


app = Flask(__name__)
app.secret_key = '5f6bf8c4462ec1be9dd0da0d59a779e6'

# Email Configuration (Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'md8855934965@gmail.com'
app.config['MAIL_PASSWORD'] = 'pzov zqyl cjhz rchw'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')  # Your portfolio HTML

@app.route('/test-image')
def test_image():
    return render_template('test.html')

@app.route('/resume')
def resume():
    return render_template('resume_mfurqan.html')  # ✅ Resume page

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(f"📥 Message received from: {name} <{email}>")

    msg = Message(subject=f"New Contact Message from {name}",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['MAIL_USERNAME']],
                  body=f"From: {name} <{email}>\n\nMessage:\n{message}")
    
    try:
        mail.send(msg)
        print("✔️ Email sent successfully!")
        flash('Message sent successfully!', 'success')
    except Exception as e:
        print("❌ Failed to send email:", str(e))
        flash('Error sending message. Please try again later.', 'danger')

    return redirect('/#contact')


if __name__ == '__main__':
    app.run(debug=True)
