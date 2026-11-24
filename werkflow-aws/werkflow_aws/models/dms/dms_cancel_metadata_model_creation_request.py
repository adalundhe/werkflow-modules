from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSCancelMetadataModelCreationRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    RequestIdentifier: StrictStr
