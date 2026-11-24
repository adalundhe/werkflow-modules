from pydantic import (
    BaseModel,
    StrictStr,
)


class AWSCredentialsSet(BaseModel):
    aws_access_key_id: StrictStr | None = None
    aws_secret_access_key: StrictStr | None = None
    aws_session_token: StrictStr | None = None
    aws_profile: StrictStr | None = None
