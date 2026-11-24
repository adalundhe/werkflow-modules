from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftClusterVersion(BaseModel):
    ClusterVersion: StrictStr | None = None
    ClusterParameterGroupFamily: StrictStr | None = None
    Description: StrictStr | None = None
