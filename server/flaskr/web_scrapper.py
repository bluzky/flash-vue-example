import requests
from bs4 import BeautifulSoup
import time
import re

class WebScrapper:
    """
    Implementation of scrapper class which per form analyzing given url
    """
    def __init__(self, url, case_sensitive = False):
        self.url = url
        self.case_sensitive = case_sensitive

        # list of words with count
        self.word_list = []
        # total word on page
        self.word_count = 0
        # total unique word on page
        self.unique_word_count = 0
        # execution time in millisecond
        self.execution_time = None

    def analyze(self):
        """Run analyzation with given URL in the constructor

        This function
            - timing execution
            - fetch document from url
            - invoke analyze_text to process retrieved document
        """
        start_time = time.time()
        text = requests.get(self.url).text
        self.analyze_text(text)
        end_time = time.time()

        # in millisecond
        self.execution_time = round(end_time - start_time, 3) * 1000

    def analyze_text(self, html):
        """ Extract text from html string and count word usage

        Args: None
        Return: None
        """
        soup = BeautifulSoup(html, features="html.parser")
        statistics = {}

        # get string from soup string genenator
        for string in soup.stripped_strings:

            # handle case sensitive option
            if not self.case_sensitive:
                string = string.lower()

            # remove special character
            clean_string= re.sub('\W+',' ', string )

            # split string into words
            for word in clean_string.split(" "):
                # skip empty word
                if word != "":
                    statistics[word] = statistics.get(word, 0) + 1
                    self.word_count += 1

        # turn dict into list and sort by usage count desc
        word_list = list(statistics.items())
        word_list.sort(reverse = True, key = lambda e: e[1])

        # update result
        self.word_list = word_list
        self.unique_word_count = len(self.word_list)

    def get_result(self):
        """ Return a result dict
        """
        return {
            "word_list": self.word_list,
            "execution_time": self.execution_time,
            "word_count": self.word_count,
            "unique_word_count": self.unique_word_count
        }


