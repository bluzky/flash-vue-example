from .database import db, Base

class AnalyzingHistory(Base):
    """Model defines columns for analyzing_history entry
    """
    __tablename__ = 'analyzing_histories'

    # analyzed url
    url = db.Column(db.String, unique=True, nullable=False)
    # execution time in ms
    execution_time = db.Column(db.Integer, default = 0)
    # time when execution completed
    completed_at = db.Column(db.DateTime, nullable=False)
    # total word count
    word_count = db.Column(db.Integer, default = 0)
    # total unique word
    unique_word_count = db.Column(db.Integer, default = 0)
    # list of [word, count]
    word_list = db.Column(db.JSON, nullable=False)

