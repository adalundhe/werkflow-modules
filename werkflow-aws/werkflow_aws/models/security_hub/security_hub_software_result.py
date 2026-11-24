from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubSoftwareResult(BaseModel):
    PackageName: StrictStr | None = None
    PackageVersion: StrictStr | None = None
    PackageType: StrictStr | None = None
    ResourceCount: StrictInt | None = None
