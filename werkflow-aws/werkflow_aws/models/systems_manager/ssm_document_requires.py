from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDocumentRequires(BaseModel):
    Name: StrictStr | None = None
    Version: StrictStr | None = None
    RequireType: StrictStr | None = None
    VersionName: StrictStr | None = None
