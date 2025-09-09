from pydantic import BaseModel, StrictStr


class AppitoCredentials(BaseModel):
    appito_access_key: StrictStr | None = None
    appito_secret_key: StrictStr | None = None