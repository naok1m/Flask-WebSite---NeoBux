from NeoStore import app
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    app.run(debug=True)