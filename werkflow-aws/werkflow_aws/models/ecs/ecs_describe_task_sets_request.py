from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSDescribeTaskSetsRequest(BaseModel):
    cluster: StrictStr
    service: StrictStr
    taskSets: list[StrictStr] | None = None
    include: list[Literal['TAGS']] | None = None
