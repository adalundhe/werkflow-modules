from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDissociatePackageRequest(BaseModel):
    PackageID: StrictStr
    DomainName: StrictStr
