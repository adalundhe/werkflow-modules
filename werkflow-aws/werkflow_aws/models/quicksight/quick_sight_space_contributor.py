from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightSpaceContributor(BaseModel):
    userName: StrictStr | None = None
    rawFileSizeBytes: StrictInt | None = None
    percentage: StrictFloat | StrictInt | None = None
