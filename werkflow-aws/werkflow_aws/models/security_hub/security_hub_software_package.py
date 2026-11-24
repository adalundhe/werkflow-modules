from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubSoftwarePackage(BaseModel):
    Name: StrictStr | None = None
    Version: StrictStr | None = None
    Epoch: StrictStr | None = None
    Release: StrictStr | None = None
    Architecture: StrictStr | None = None
    PackageManager: StrictStr | None = None
    FilePath: StrictStr | None = None
    FixedInVersion: StrictStr | None = None
    Remediation: StrictStr | None = None
    SourceLayerHash: StrictStr | None = None
    SourceLayerArn: StrictStr | None = None
