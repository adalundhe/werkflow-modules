from __future__ import annotations
from pydantic import BaseModel
from .glacier_csv_output import GlacierCSVOutput


class GlacierOutputSerialization(BaseModel):
    csv: GlacierCSVOutput | None = None
