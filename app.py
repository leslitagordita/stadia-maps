import re
from flask import Flask, redirect, request, render_template, session, send_from_directory
from flask_session import Session
from geojson import Point

app=Flask(__name__)

if __name__ == '__main__':
    app.debug=True
    app.run()



