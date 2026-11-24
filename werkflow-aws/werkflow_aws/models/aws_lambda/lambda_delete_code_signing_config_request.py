from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaDeleteCodeSigningConfigRequest(BaseModel):
    CodeSigningConfigArn: StrictStr
