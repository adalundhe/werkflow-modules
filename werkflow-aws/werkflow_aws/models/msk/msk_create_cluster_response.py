from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKCreateClusterResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterName: StrictStr | None = None
    State: StrictStr | None = None
