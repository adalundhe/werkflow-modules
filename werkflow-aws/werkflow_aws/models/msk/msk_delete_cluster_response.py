from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteClusterResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    State: StrictStr | None = None
