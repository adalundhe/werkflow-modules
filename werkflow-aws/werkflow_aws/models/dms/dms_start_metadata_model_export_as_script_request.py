from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DMSStartMetadataModelExportAsScriptRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    SelectionRules: StrictStr
    Origin: Literal['SOURCE', 'TARGET']
    FileName: StrictStr | None = None
