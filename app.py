"""Flask web application for Web Compliance Checker"""

from flask import Flask, render_template, request, jsonify
from scanner import scan_website
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    """Home page with URL input form"""
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    """API endpoint for scanning websites"""
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        result = scan_website(url)
        
        return jsonify({
            'success': True,
            'url': url,
            'results': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/results', methods=['GET', 'POST'])
def results():
    """Results page"""
    try:
        # Handle both GET and POST requests
        if request.method == 'POST':
            url = request.form.get('url', '').strip()
        else:
            url = request.args.get('url', '').strip()
        
        if not url:
            return render_template('index.html', error='URL is required')
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        result = scan_website(url)
        
        return render_template('result.html', url=url, results=result)
    
    except Exception as e:
        return render_template('index.html', error=f'Error scanning website: {str(e)}')


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
