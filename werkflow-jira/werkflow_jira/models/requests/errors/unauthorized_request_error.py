class UnauthorizedRequestError(Exception):

    def __init__(
        self,
        url: str,
        method: str,
        status: int
    ) -> None:
        super().__init__(
            f'Client is not authorized to make {method} request to {url} (encountered {status})'
        )