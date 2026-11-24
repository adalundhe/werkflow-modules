from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDocumentDefaultVersionDescription(BaseModel):
    Name: StrictStr | None = None
    DefaultVersion: StrictStr | None = None
    DefaultVersionName: StrictStr | None = None
