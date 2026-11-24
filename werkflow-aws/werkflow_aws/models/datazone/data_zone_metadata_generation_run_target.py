from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMetadataGenerationRunTarget(BaseModel):
    type: StrictStr | None = None
    identifier: StrictStr | None = None
    revision: StrictStr | None = None
