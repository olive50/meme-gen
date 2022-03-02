"""This class is used to import quotes from csv file."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class used for CSV processing."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file.

        Arguments:
        path -- the path to the file.

        return :
        a list of quotes from  the file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
