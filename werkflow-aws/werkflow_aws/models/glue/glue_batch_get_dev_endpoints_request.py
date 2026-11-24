from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetDevEndpointsRequest(BaseModel):
    DevEndpointNames: list[StrictStr]
