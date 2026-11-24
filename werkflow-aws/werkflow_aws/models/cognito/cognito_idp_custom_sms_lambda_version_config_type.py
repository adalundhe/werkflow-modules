from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPCustomSMSLambdaVersionConfigType(BaseModel):
    LambdaVersion: StrictStr | None = None
    LambdaArn: StrictStr | None = None
