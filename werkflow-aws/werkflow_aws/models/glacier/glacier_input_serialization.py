from __future__ import annotations
from pydantic import BaseModel
from .glacier_csv_input import GlacierCSVInput


class GlacierInputSerialization(BaseModel):
    csv: GlacierCSVInput | None = None
