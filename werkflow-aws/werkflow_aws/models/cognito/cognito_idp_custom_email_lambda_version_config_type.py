from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCustomEmailLambdaVersionConfigType(BaseModel):
    LambdaVersion: StrictStr | None = None
    LambdaArn: StrictStr | None = None
