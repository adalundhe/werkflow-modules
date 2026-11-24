from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKGetCompatibleKafkaVersionsRequest(BaseModel):
    ClusterArn: StrictStr | None = None
