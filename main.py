from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)
# email config uncomment bottom code when done
# app.config['MAIL_SERVER']= 'localhost'
# app.config['MAIL_PORT'] = 25
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_DEBUG'] = app.debug
# app.config['MAIL_USERNAME'] = None
# app.config['MAIL_PASSWORD'] = None
# app.config['MAIL_DEFAULT_SENDER'] = None
# app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = app.testing
# app.config['MAIL_ASCII_ATTACHMENTS'] = False
# mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #once server config is done uncomment the code below leave the return message or change it to a flash or a redirect for all url routes
    # with mail.connect() as conn:
    #     for user in users:
    #         message = '...'
    #         subject = "hello, %s" % user.name
    #         msg = Message(recipients=[user.email],
    #                     body=message,
    #                     subject=subject)
    #         conn.send(msg)
            return 'message sent'
    return render_template('index.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
    # with mail.connect() as conn:
    #     for user in users:
    #         message = '...'
    #         subject = "hello, %s" % user.name
    #         msg = Message(recipients=[user.email],
    #                     body=message,
    #                     subject=subject)
    #         conn.send(msg)
            return 'message sent'
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
    # with mail.connect() as conn:
    #     for user in users:
    #         message = '...'
    #         subject = "hello, %s" % user.name
    #         msg = Message(recipients=[user.email],
    #                     body=message,
    #                     subject=subject)
    #         conn.send(msg)
            return 'message sent'
    return render_template('contact.html')


@app.route('/our/services', methods=['POST', 'GET'])
def services():
    if request.method == 'POST':
    # with mail.connect() as conn:
    #     for user in users:
    #         message = '...'
    #         subject = "hello, %s" % user.name
    #         msg = Message(recipients=[user.email],
    #                     body=message,
    #                     subject=subject)
    #         conn.send(msg)
            return 'message sent'
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)