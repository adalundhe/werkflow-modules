from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftRebootClusterRequest(BaseModel):
    ClusterIdentifier: StrictStr
