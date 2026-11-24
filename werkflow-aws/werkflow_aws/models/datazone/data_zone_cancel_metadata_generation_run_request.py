from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCancelMetadataGenerationRunRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
