from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_csv_input import AWSS3CSVInput
from .awss3_json_input import AWSS3JSONInput
from .awss3_parquet_input import AWSS3ParquetInput


class AWSS3InputSerialization(BaseModel):
    CSV: AWSS3CSVInput | None = None
    CompressionType: Literal['NONE', 'GZIP', 'BZIP2'] | None = None
    JSON: AWSS3JSONInput | None = None
    Parquet: AWSS3ParquetInput | None = None
