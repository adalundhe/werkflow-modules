from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GuardDutyFindingTypeClassification(BaseModel):
    FindingType: StrictStr | None = None
    Classification: StrictStr | None = None
    Count: StrictInt | None = None
    Percentage: StrictFloat | StrictInt | None = None
    Description: StrictStr | None = None
