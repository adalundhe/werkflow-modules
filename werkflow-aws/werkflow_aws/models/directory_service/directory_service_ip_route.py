from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceIpRoute(BaseModel):
    CidrIp: StrictStr | None = None
    CidrIpv6: StrictStr | None = None
    Description: StrictStr | None = None
