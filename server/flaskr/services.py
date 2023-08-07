from flaskr import web_scrapper
from .database import db
from .models import AnalyzingHistory
from datetime import timezone, datetime

# TODO: move this to configuration
CACHE_TTL = 6 * 3600 # 6 hours

def analyze_url(url, ignore_cache=False):
    """Business logic for analyzing url

    Args:
        url: url for analyzing
        ignore_cache: flag to ignore cache and re-run analyzing process

    Return:
        A dict with following structur
        cached: bool flag to indicate if this result is loaded from cache or not
        entry: history entry from database
    """
    # forst look up history for existing url
    history_entry = db.session.query(AnalyzingHistory).filter_by(url = url).one_or_none()

    # check url is saved and not ignore cache
    if history_entry and not ignore_cache:
        delta = datetime.utcnow() - history_entry.completed_at

        # only return result if CACHE_TTL is not expired
        if delta.total_seconds() < CACHE_TTL:
            return {"cached": True, "entry": history_entry}

    # run analyzing
    scrapper = web_scrapper.WebScrapper(url)
    scrapper.analyze()
    result = scrapper.get_result()

    # build data dict for insert/update
    data_dict = {
        "url": url,
        "execution_time": result["execution_time"],
        "completed_at": datetime.now(tz=timezone.utc),
        "word_count": result["word_count"],
        "unique_word_count": result["unique_word_count"],
        "word_list": result["word_list"]
    }

    # update existing record
    if history_entry:
        for key, value in data_dict.items():
            setattr(history_entry, key, value)
    else:
        # insert database
        history_entry = AnalyzingHistory(**data_dict)
        db.session.add(history_entry)

    db.session.commit()
    db.session.refresh(history_entry)

    return {"cached": False, "entry": history_entry}
