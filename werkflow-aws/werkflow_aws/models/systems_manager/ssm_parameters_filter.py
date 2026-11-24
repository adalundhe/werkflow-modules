from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMParametersFilter(BaseModel):
    Key: Literal['Name', 'Type', 'KeyId']
    Values: list[StrictStr]
