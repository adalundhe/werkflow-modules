from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexTestSetExportSpecification(BaseModel):
    testSetId: StrictStr | None = None
