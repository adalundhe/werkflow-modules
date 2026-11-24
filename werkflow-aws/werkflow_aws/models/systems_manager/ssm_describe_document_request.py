from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDescribeDocumentRequest(BaseModel):
    Name: StrictStr
    DocumentVersion: StrictStr | None = None
    VersionName: StrictStr | None = None
