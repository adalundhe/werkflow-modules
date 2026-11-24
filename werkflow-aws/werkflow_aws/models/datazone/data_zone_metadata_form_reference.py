from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneMetadataFormReference(BaseModel):
    typeIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
