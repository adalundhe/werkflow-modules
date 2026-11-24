from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKGetBootstrapBrokersRequest(BaseModel):
    ClusterArn: StrictStr | None = None
