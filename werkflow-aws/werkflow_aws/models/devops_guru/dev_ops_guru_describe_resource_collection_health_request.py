from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeResourceCollectionHealthRequest(BaseModel):
    ResourceCollectionType: Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
    NextToken: StrictStr | None = None
