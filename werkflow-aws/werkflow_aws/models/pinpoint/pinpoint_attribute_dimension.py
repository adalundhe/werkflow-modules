from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointAttributeDimension(BaseModel):
    AttributeType: StrictStr | None = None
    Values: list[StrictStr] | None = None
