from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AppFlowSourceFieldProperties(BaseModel):
    isRetrievable: StrictBool | None = None
    isQueryable: StrictBool | None = None
    isTimestampFieldForIncrementalQueries: StrictBool | None = None
