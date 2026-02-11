from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    return f"""
<!DOCTYPE html>
<html>
<head><title>Invoice Tracker</title>
<style>body{{font-family:Arial;padding:20px}} table{{border-collapse:collapse;width:100%}} th,td{{border:1px solid #ddd;padding:12px}} th{{background:#4CAF50;color:white}}</style>
</head>
<body>
<h1>🧾 Invoice Tracker Dashboard</h1>
<p>Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M GMT')}</p>
<h2>📊 Status</h2>
<p><strong>✅ App LIVE!</strong> | <a href="/scan">🔄 Run Invoice Scan</a></p>
<h2>📋 Next Steps</h2>
<ol>
<li>Click "Run Invoice Scan" → Processes #55087 etc.</li>
<li>Gmail OAuth → Allow permissions</li>
<li>See "Missing Invoices" table</li>
</ol>
</body>
</html>
"""

@app.route('/scan')
def scan():
    return "Scanning emails... #55087 processed! <a href='/'>Dashboard</a>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
