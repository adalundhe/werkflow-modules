from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerTag(BaseModel):
    Key: StrictStr
    Value: StrictStr
