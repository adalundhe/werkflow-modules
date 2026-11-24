from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_csv_input_model import AWSS3CSVInputModel
from .awss3_json_input_model import AWSS3JSONInputModel
from .awss3_parquet_input_model import AWSS3ParquetInputModel


class AWSS3InputSerializationModel(BaseModel):
    CSV: AWSS3CSVInputModel | None = None
    CompressionType: Literal['NONE', 'GZIP', 'BZIP2'] | None = None
    JSON: AWSS3JSONInputModel | None = None
    Parquet: AWSS3ParquetInputModel | None = None
