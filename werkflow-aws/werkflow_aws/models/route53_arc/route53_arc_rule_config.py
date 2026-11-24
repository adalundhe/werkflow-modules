from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class Route53ARCRuleConfig(BaseModel):
    Inverted: StrictBool | None = None
    Threshold: StrictInt | None = None
    Type: StrictStr | None = None
