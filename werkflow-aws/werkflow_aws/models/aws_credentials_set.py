from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Optional


class AWSCredentialsSet(BaseModel):
    aws_access_key_id: StrictStr
    aws_secret_access_key: StrictStr
    aws_session_token: StrictStr