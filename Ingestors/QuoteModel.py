"""This is a model class representing a quote."""


class QuoteModel():
    """Class quote with body text and author."""

    def __init__(self, body, author):
        """Instanciate an object quote."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Representation of a quote."""
        return f"{self.body}, {self.author}"
