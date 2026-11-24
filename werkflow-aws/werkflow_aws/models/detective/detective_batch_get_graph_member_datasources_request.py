from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveBatchGetGraphMemberDatasourcesRequest(BaseModel):
    GraphArn: StrictStr
    AccountIds: list[StrictStr]
