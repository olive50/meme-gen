from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        with open(path, "r") as file:
            lines = file.readlines()
            quotes = [QuoteModel(*quote.strip("\n").split(" - ")) for quote in lines]
            return quotes