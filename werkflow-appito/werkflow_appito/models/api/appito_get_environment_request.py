from pydantic import BaseModel, StrictStr


class AppitoGetEnviornmentRequest(BaseModel):
    auth_token: StrictStr
    domain: StrictStr
    environment_id: StrictStr | None = None