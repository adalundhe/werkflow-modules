class MethodNotAllowedError(Exception):

    def __init__(
        self,
        url: str,
        method: str,
        status: int
    ) -> None:
        super().__init__(
            f'Method {method} for request to {url} is not allowed (encountered {status})'
        )