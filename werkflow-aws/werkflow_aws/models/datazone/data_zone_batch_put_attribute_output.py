from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneBatchPutAttributeOutput(BaseModel):
    attributeIdentifier: StrictStr | None = None
