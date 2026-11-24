from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SESDomainIspPlacement(BaseModel):
    IspName: StrictStr | None = None
    InboxRawCount: StrictInt | None = None
    SpamRawCount: StrictInt | None = None
    InboxPercentage: StrictFloat | StrictInt | None = None
    SpamPercentage: StrictFloat | StrictInt | None = None
