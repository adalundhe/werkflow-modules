from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailInstancePortInfo(BaseModel):
    fromPort: StrictInt | None = None
    toPort: StrictInt | None = None
    protocol: StrictStr | None = None
    accessFrom: StrictStr | None = None
    accessType: StrictStr | None = None
    commonName: StrictStr | None = None
    accessDirection: StrictStr | None = None
    cidrs: list[StrictStr] | None = None
    ipv6Cidrs: list[StrictStr] | None = None
    cidrListAliases: list[StrictStr] | None = None
