from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveBatchGetMembershipDatasourcesRequest(BaseModel):
    GraphArns: list[StrictStr]
