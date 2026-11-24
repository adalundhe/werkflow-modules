from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSStartExtensionPackAssociationRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
