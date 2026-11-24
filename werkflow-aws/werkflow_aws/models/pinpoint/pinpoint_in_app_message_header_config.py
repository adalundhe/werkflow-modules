from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointInAppMessageHeaderConfig(BaseModel):
    Alignment: StrictStr | None = None
    Header: StrictStr | None = None
    TextColor: StrictStr | None = None
