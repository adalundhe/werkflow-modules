class UnprocessableContentError(Exception):

    def __init__(
        self,
        url: str,
        method: str,
        status: int
    ) -> None:
        super().__init__(
            f"Client encountered {status} status while making {method} request to {url}.\nBe sure to check whether the data you're sending is what the server expects!"
        )