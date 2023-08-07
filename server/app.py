from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flaskr import forms, services
from flaskr import db
import os


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

# initialize database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lemon.sqlite"
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/analyze', methods=['GET'])
def analyze():
    """Analyze given url and return top 100 most used words

    Parameters:
        url (string) [required]: url to fetch content
        ignore_cache (boolean): A flag to ignore cached data and run a fresh analyzing. Default to False.

    Sucess response:
        data: data object
            url: analyzed url
            execution_time: analyzing execution time (fetching url and analyze text only)
            completed_at: datetime of analyzing completion
            word_count [int]: total word on page
            unique_word_count [int]: number of unique word on page
            top_words: top 100 most used word. Each item is an array of 2 items [word, count]

    Error respose:
        errors: error map, with key is field name and value is list of field errors.
    """
    form = forms.AnalyzeForm(request.args, meta={'csrf': False})
    if form.validate():
        result = services.analyze_url(form.url.data, form.ignore_cache.data)
        cached, entry = result.values()
        data = {
            "url": entry.url,
            "cached": cached,
            "execution_time": entry.execution_time,
            "completed_at": entry.completed_at,
            "word_count": entry.word_count,
            "unique_word_count": entry.unique_word_count,
            "top_words": entry.word_list[0:100]
        }
        return jsonify({"data": data})

    return  {
        "errors": form.errors
    }, 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
