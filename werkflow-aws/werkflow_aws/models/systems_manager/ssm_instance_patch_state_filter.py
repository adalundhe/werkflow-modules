from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMInstancePatchStateFilter(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
    Type: Literal['Equal', 'NotEqual', 'LessThan', 'GreaterThan']
