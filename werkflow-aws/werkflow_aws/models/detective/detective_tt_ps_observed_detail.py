from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DetectiveTTPsObservedDetail(BaseModel):
    Tactic: StrictStr | None = None
    Technique: StrictStr | None = None
    Procedure: StrictStr | None = None
    IpAddress: StrictStr | None = None
    APIName: StrictStr | None = None
    APISuccessCount: StrictInt | None = None
    APIFailureCount: StrictInt | None = None
