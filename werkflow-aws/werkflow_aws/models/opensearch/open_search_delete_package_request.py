from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeletePackageRequest(BaseModel):
    PackageID: StrictStr
