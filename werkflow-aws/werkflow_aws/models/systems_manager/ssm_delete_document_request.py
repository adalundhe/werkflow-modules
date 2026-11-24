from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMDeleteDocumentRequest(BaseModel):
    Name: StrictStr
    DocumentVersion: StrictStr | None = None
    VersionName: StrictStr | None = None
    Force: StrictBool | None = None
