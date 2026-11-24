from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveRelatedFindingGroupDetail(BaseModel):
    Id: StrictStr | None = None
