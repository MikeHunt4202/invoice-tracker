from flask import Flask
app = Flask(__name__)

@app.route('/')
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head><title>🧾 Invoice Tracker</title>
<style>body{font-family:sans-serif;max
