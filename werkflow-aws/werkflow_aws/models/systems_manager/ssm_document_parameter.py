from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDocumentParameter(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    DefaultValue: StrictStr | None = None
