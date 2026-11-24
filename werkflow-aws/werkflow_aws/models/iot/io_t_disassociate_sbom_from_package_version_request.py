from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDisassociateSbomFromPackageVersionRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
    clientToken: StrictStr | None = None
