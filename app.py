from flask import Flask, render_template, request
from track import get_manuscript_info, format_timestamp, process_review_timeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    manuscript_data = None
    error = None
    
    if request.method == 'POST':
        uuid = request.form.get('uuid')
        if uuid:
            manuscript_data = get_manuscript_info(uuid)
            if manuscript_data is None:
                error = "Unable to fetch manuscript information. Please check the UUID and try again."
    
    return render_template('index.html', 
                         manuscript_data=manuscript_data, 
                         format_timestamp=format_timestamp,
                         process_review_timeline=process_review_timeline,
                         error=error)

if __name__ == '__main__':
    app.run(debug=True) 