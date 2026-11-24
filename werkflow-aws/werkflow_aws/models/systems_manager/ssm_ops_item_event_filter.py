from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMOpsItemEventFilter(BaseModel):
    Key: Literal['OpsItemId']
    Values: list[StrictStr]
    Operator: Literal['Equal']
