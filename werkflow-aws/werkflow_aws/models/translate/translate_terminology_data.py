from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class TranslateTerminologyData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    File: StrictBytes | BinaryIO | StrictStr
    Format: Literal['CSV', 'TMX', 'TSV']
    Directionality: Literal['UNI', 'MULTI'] | None = None
