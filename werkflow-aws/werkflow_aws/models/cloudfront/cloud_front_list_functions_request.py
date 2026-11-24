from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontListFunctionsRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    Stage: Literal['DEVELOPMENT', 'LIVE'] | None = None
