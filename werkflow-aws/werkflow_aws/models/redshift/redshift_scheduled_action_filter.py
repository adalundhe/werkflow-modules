from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftScheduledActionFilter(BaseModel):
    Name: Literal['cluster-identifier', 'iam-role']
    Values: list[StrictStr]
