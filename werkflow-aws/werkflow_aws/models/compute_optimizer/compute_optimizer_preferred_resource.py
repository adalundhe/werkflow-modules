from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerPreferredResource(BaseModel):
    name: Literal['Ec2InstanceTypes'] | None = None
    includeList: list[StrictStr] | None = None
    excludeList: list[StrictStr] | None = None
