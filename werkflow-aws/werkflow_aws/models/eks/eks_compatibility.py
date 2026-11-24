from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSCompatibility(BaseModel):
    clusterVersion: StrictStr | None = None
    platformVersions: list[StrictStr] | None = None
    defaultVersion: StrictBool | None = None
