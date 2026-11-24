from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointInAppMessageBodyConfig(BaseModel):
    Alignment: StrictStr | None = None
    Body: StrictStr | None = None
    TextColor: StrictStr | None = None
