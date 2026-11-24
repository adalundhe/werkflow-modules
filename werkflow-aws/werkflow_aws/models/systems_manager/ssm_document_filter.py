from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMDocumentFilter(BaseModel):
    key: Literal['Name', 'Owner', 'PlatformTypes', 'DocumentType']
    value: StrictStr
