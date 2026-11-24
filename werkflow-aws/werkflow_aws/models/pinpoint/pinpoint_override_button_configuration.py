from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointOverrideButtonConfiguration(BaseModel):
    ButtonAction: StrictStr | None = None
    Link: StrictStr | None = None
