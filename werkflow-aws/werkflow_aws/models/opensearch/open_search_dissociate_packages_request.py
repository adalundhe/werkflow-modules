from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDissociatePackagesRequest(BaseModel):
    PackageList: list[StrictStr]
    DomainName: StrictStr
