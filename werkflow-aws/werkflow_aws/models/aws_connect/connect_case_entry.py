from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCaseEntry(BaseModel):
    CaseId: StrictStr | None = None
    CaseReferenceNumber: StrictStr | None = None
