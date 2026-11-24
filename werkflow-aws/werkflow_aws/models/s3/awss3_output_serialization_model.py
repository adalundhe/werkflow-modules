from __future__ import annotations
from pydantic import BaseModel
from .awss3_csv_output_model import AWSS3CSVOutputModel
from .awss3_json_output_model import AWSS3JSONOutputModel


class AWSS3OutputSerializationModel(BaseModel):
    CSV: AWSS3CSVOutputModel | None = None
    JSON: AWSS3JSONOutputModel | None = None
