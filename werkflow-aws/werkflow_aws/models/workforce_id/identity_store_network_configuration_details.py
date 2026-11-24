from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IdentityStoreNetworkConfigurationDetails(BaseModel):
    VpceAccessRequired: StrictBool | None = None
    ApiRestrictSourceVpcs: list[StrictStr] | None = None
    ApiAllowSourceIps: list[StrictStr] | None = None
    ScimAllowSourceIps: list[StrictStr] | None = None
