from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSStartMetadataModelConversionRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
