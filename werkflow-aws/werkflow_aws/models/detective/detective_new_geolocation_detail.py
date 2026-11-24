from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DetectiveNewGeolocationDetail(BaseModel):
    Location: StrictStr | None = None
    IpAddress: StrictStr | None = None
    IsNewForEntireAccount: StrictBool | None = None
