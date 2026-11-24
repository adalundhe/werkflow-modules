from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactLensRedactionConfiguration(BaseModel):
    Behavior: StrictStr | None = None
    Policy: StrictStr | None = None
    Entities: list[StrictStr] | None = None
    MaskMode: StrictStr | None = None
