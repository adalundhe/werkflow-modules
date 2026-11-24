from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessBatchGetVpcEndpointRequest(BaseModel):
    ids: list[StrictStr]
