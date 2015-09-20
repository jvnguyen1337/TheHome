from flask              import Flask, render_template, flash, jsonify, request
from flask_bootstrap    import Bootstrap
from flask_appconfig    import AppConfig
from flask_wtf          import Form, RecaptchaField
from flask_wtf.file     import FileField
from wtforms            import TextField, HiddenField, ValidationError, RadioField,\
                        BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required
#from GPIO               import board

# False - lights are off, True lights are on
lights_dict = {"kitchen":False, "hall":False, "tank":False}

def lights_dict_set(pin, lights_dict):
    if pin == 12:
        lights_dict["hall"]    = True
    elif pin == 19:
        lights_dict["kitchen"] = True
    elif pin == 13:
        lights_dict["tank"]    = True

    elif pin == 16:
        lights_dict["hall"]    = False
    elif pin == 15:
        lights_dict["kitchen"] = False
    elif pin == 11:
        lights_dict["tank"]    = False

    return lights_dict

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
   # app.config['SERVER_NAME'] = 'home:80'

    @app.route('/board/<pin>')
    def board(pin):
        #ajax_request = request.args.get('ajax_request', 0, type=str)
        #board(int(pin))
        print "wassup!\n", pin, type(int(pin))

        return jsonify(lights=lights_dict_set(int(pin), lights_dict))

    @app.route('/', methods=('GET', 'POST'))
    def index():
        return render_template('index.html')
    return app

if __name__ == '__main__':
    create_app().run(debug = True, host="0.0.0.0")
