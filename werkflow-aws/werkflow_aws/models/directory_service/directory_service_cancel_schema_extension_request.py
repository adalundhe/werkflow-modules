from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceCancelSchemaExtensionRequest(BaseModel):
    DirectoryId: StrictStr
    SchemaExtensionId: StrictStr
