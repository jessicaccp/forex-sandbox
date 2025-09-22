class SameCurrencyError(Exception):
    """Raised when from_currency and to_currency are the same."""

    def __init__(
        self,
        message: str = "'from_currency' and 'to_currency' cannot be the same.",
    ):
        self.message = message
        super().__init__(self.message)
