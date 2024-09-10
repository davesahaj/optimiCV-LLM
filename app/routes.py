from flask import request, jsonify
from app import app
import pdfplumber


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    


    # do LLM function calls here (/main.py stuff)
    
    # Also, modify LLM code of main.py with below lines
    #  
    # file_extractor = {".pdf": parser}
    # file_reader = SimpleFileReader(file, file_extractor=file_extractor)
    # document = file_reader.load_data()

    # this is a placeholder code, it converts the file into text and returns the text from PDF.
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    


    return jsonify({'text': text}), 200

if __name__ == '__main__':
    app.run(port=5000)

