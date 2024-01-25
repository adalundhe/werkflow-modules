class EmptyResponseException(Exception):

    def __init__(
        self,
        service_name: str,
        call_name: str,
        retrieval_item_name: str
    ) -> None:
        super().__init__(
            f'Err. - call to - {call_name} - for service - {service_name} - failed to retrieve - {retrieval_item_name} - and returned None.'
        )