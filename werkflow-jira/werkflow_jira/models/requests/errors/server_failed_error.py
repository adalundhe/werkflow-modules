class ServerFailedError(Exception):

    def __init__(
        self,
        url: str,
        method: str,
        status: int
    ) -> None:
        super().__init__(
            f'Server encountered {status} status while making {method} request to {url}'
        )