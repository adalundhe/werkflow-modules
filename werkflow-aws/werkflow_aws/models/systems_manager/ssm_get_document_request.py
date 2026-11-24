from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMGetDocumentRequest(BaseModel):
    Name: StrictStr
    VersionName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    DocumentFormat: Literal['YAML', 'JSON', 'TEXT'] | None = None
