from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2TagFieldSpecificationRequest(BaseModel):
    ResourceType: Literal['network-interface', 'instance', 'auto-scaling-group'] | None = None
    TagKeys: list[StrictStr] | None = None
