from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AthenaGetSystemTableConfigurationRequest(BaseModel):
    TableName: Literal['ALL']
