from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDeleteSourceCredentialsRequest(BaseModel):
    arn: StrictStr
