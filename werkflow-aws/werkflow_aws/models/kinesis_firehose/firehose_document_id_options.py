from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseDocumentIdOptions(BaseModel):
    DefaultDocumentIdFormat: StrictStr | None = None
