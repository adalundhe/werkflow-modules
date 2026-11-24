from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSDescribeTaskDefinitionRequest(BaseModel):
    taskDefinition: StrictStr
    include: list[Literal['TAGS']] | None = None
