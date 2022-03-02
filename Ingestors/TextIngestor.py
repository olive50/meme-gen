"""This class is used to import quotes from text file."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """Class used for txt processing."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """Parse txt file.

        Arguments:
        path -- the path to the file.

        return :
        a list of quotes from  the file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        with open(path, "r") as file:
            lines = file.readlines()
            quotes = [QuoteModel(*quote.strip("\n").split(" - "))
                      for quote in lines]
            return quotes
