from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruUpdateTagCollectionFilter(BaseModel):
    AppBoundaryKey: StrictStr
    TagValues: list[StrictStr]
