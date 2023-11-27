import webview

from ui_webview.flask import flask_app

def app():
    webview.create_window('Flask example', flask_app)  
    webview.start()
