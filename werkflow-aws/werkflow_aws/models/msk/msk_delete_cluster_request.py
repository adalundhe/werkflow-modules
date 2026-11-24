from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteClusterRequest(BaseModel):
    ClusterArn: StrictStr | None = None
    CurrentVersion: StrictStr | None = None
