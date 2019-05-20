from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_ow_four(error):
    '''
    Function to render 404 error
    '''
    return render_template('fourOwfour.html'), 404