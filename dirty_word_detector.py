import requests
import json
from bs4 import BeautifulSoup

class DirtyWordDetector():
    """
    Contain various methods to detect dirty words and suggest alternatives.
    """
    def __init__(self):
        """
        Class constructor.
        """
        with open("dirty_words.json", encoding="UTF-8") as json_file:
            self._dirty_json = json.load(json_file)
        self.dirty_words = [record["word"]
                            for record in self._dirty_json["RECORDS"]]

    def is_dirty(self, word):
        """
        Check either a word is dirty or not.

        Arguments
        ---------
        word : string
            The word tested

        Returns
        -------
        bool
            True if the word is a dirty word, False else
        """
        return word in self.dirty_words

    def get_synonyms(self, word):
        """
        
        """
        url = f"http://www.synonymo.fr/synonyme/{word}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        afields = soup.find_all('a')
        last_pos = 1
        for i, elt in enumerate(afields):
            if elt.text[:9] == "Antonymes":
                last_pos = i
        return [content.text for content in afields[1:last_pos]]

    def get_undirty_synonyms(self, word):
        synonyms = self.get_synonyms(word)
        return [word for word in synonyms if not self.is_dirty(word)]
