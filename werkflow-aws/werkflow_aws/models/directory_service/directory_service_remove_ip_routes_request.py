from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRemoveIpRoutesRequest(BaseModel):
    DirectoryId: StrictStr
    CidrIps: list[StrictStr] | None = None
    CidrIpv6s: list[StrictStr] | None = None
