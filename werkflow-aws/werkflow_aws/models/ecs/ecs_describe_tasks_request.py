from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSDescribeTasksRequest(BaseModel):
    tasks: list[StrictStr]
    cluster: StrictStr | None = None
    include: list[Literal['TAGS']] | None = None
