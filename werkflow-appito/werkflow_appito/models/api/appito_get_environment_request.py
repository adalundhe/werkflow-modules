from pydantic import BaseModel, StrictStr


class AppitoGetEnvironmentRequest(BaseModel):
    auth_token: StrictStr
    domain: StrictStr
    environment_id: StrictStr | None = None


AppitoGetEnviornmentRequest = AppitoGetEnvironmentRequest
