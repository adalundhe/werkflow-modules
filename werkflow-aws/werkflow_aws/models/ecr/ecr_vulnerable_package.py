from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRVulnerablePackage(BaseModel):
    arch: StrictStr | None = None
    epoch: StrictInt | None = None
    filePath: StrictStr | None = None
    name: StrictStr | None = None
    packageManager: StrictStr | None = None
    release: StrictStr | None = None
    sourceLayerHash: StrictStr | None = None
    version: StrictStr | None = None
    fixedInVersion: StrictStr | None = None
