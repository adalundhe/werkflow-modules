from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneRedshiftClusterStorage(BaseModel):
    clusterName: StrictStr | None = None
