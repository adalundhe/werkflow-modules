from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPPreTokenGenerationVersionConfigType(BaseModel):
    LambdaVersion: StrictStr | None = None
    LambdaArn: StrictStr | None = None
