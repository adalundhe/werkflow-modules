from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSStartMetadataModelExportToTargetRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
    OverwriteExtensionPack: StrictBool | None = None
