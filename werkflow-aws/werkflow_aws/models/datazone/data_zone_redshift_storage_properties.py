from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneRedshiftStorageProperties(BaseModel):
    clusterName: StrictStr | None = None
    workgroupName: StrictStr | None = None
