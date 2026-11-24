from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IdentityStoreNetworkConfiguration(BaseModel):
    VpceAccessRequired: StrictBool
    ApiRestrictSourceVpcs: list[StrictStr] | None = None
    ApiAllowSourceIps: list[StrictStr] | None = None
    ScimAllowSourceIps: list[StrictStr] | None = None
