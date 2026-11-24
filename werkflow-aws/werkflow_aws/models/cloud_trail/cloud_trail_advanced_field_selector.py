from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailAdvancedFieldSelector(BaseModel):
    Field: StrictStr | None = None
    Equals: list[StrictStr] | None = None
    StartsWith: list[StrictStr] | None = None
    EndsWith: list[StrictStr] | None = None
    NotEquals: list[StrictStr] | None = None
    NotStartsWith: list[StrictStr] | None = None
    NotEndsWith: list[StrictStr] | None = None
