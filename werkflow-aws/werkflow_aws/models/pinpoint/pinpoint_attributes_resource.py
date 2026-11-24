from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointAttributesResource(BaseModel):
    ApplicationId: StrictStr | None = None
    AttributeType: StrictStr | None = None
    Attributes: list[StrictStr] | None = None
