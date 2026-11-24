from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZonePackageConfig(BaseModel):
    packageManager: StrictStr | None = None
    packageSpecification: StrictStr | None = None
