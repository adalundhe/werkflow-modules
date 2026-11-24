from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyListInvestigationRecordsRequest(BaseModel):
    DetectorId: StrictStr
    InvestigationId: StrictStr
    RecordTypes: list[Literal['OBSERVATION', 'ANALYSIS', 'UPDATE', 'FETCH', 'METADATA']] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
