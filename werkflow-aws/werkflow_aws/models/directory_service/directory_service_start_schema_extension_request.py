from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DirectoryServiceStartSchemaExtensionRequest(BaseModel):
    DirectoryId: StrictStr
    CreateSnapshotBeforeSchemaExtension: StrictBool
    LdifContent: StrictStr
    Description: StrictStr
