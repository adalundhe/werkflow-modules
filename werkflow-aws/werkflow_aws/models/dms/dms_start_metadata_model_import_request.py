from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class DMSStartMetadataModelImportRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
    Origin: Literal['SOURCE', 'TARGET']
    Refresh: StrictBool | None = None
