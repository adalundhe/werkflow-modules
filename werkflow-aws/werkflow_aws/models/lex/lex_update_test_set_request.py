from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexUpdateTestSetRequest(BaseModel):
    testSetId: StrictStr
    testSetName: StrictStr
    description: StrictStr | None = None
