from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TranslateGetTerminologyRequest(BaseModel):
    Name: StrictStr
    TerminologyDataFormat: Literal['CSV', 'TMX', 'TSV'] | None = None
