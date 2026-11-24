from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontListConnectionFunctionsRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Stage: Literal['DEVELOPMENT', 'LIVE'] | None = None
