from __future__ import annotations
from pydantic import BaseModel
from .awss3_csv_output import AWSS3CSVOutput
from .awss3_json_output import AWSS3JSONOutput


class AWSS3OutputSerialization(BaseModel):
    CSV: AWSS3CSVOutput | None = None
    JSON: AWSS3JSONOutput | None = None
