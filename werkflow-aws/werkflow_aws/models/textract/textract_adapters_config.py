from __future__ import annotations
from pydantic import BaseModel
from .textract_adapter import TextractAdapter


class TextractAdaptersConfig(BaseModel):
    Adapters: list[TextractAdapter]
