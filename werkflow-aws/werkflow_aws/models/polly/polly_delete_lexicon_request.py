from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyDeleteLexiconRequest(BaseModel):
    Name: StrictStr
