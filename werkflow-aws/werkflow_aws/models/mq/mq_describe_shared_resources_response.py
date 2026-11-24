from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .mq_shared_resource import MQSharedResource


class MQDescribeSharedResourcesResponse(BaseModel):
    NextToken: StrictStr | None = None
    SharedResources: list[MQSharedResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
