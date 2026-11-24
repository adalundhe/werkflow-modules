from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ListTagsForResourcesRequest(BaseModel):
    ResourceType: Literal['healthcheck', 'hostedzone', 'healthchecksource']
    ResourceIds: list[StrictStr]
