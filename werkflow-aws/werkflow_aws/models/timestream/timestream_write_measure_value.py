from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TimestreamWriteMeasureValue(BaseModel):
    Name: StrictStr
    Value: StrictStr
    Type: Literal['DOUBLE', 'BIGINT', 'VARCHAR', 'BOOLEAN', 'TIMESTAMP', 'MULTI']
