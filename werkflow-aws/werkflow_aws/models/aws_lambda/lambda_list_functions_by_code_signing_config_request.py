from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListFunctionsByCodeSigningConfigRequest(BaseModel):
    CodeSigningConfigArn: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
