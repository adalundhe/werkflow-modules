from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSDescribeContainerInstancesRequest(BaseModel):
    containerInstances: list[StrictStr]
    cluster: StrictStr | None = None
    include: list[Literal['TAGS', 'CONTAINER_INSTANCE_HEALTH']] | None = None
