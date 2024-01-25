class UnsetAWSConnectionException(Exception):

    def __init__(
        self,
        service_name: str
    ) -> None:
        super().__init__(
            f'Err. - {service_name} - connection has not been created. Please call - connect() - before executing any other operations.'
        )