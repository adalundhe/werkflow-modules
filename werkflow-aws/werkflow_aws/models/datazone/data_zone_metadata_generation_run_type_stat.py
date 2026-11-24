from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMetadataGenerationRunTypeStat(BaseModel):
    type: StrictStr | None = None
    status: StrictStr | None = None
    errorMessage: StrictStr | None = None
