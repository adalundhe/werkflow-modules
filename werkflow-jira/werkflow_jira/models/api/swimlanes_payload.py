from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swimlane_payload import SwimlanePayload


class SwimlanesPayload(BaseModel):
    customSwimlanes: list[SwimlanePayload] | None = None
    defaultCustomSwimlaneName: StrictStr | None = None
    swimlaneStrategy: StrictStr | None = None
