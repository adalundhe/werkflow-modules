class ResourceNotFoundError(Exception):

    def __init__(
        self,
        url: str,
        method: str,
        status: int
    ) -> None:
        super().__init__(
            f'Resource {url} was not found for {method} request (returned {status})'
        )