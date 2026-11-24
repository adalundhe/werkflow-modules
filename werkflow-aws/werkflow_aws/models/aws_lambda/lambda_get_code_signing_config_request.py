from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaGetCodeSigningConfigRequest(BaseModel):
    CodeSigningConfigArn: StrictStr
