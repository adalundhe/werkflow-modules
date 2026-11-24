from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_open_id_connect_group_configuration import VerifiedPermissionsOpenIdConnectGroupConfiguration
from .verified_permissions_open_id_connect_token_selection import VerifiedPermissionsOpenIdConnectTokenSelection


class VerifiedPermissionsOpenIdConnectConfiguration(BaseModel):
    issuer: StrictStr
    tokenSelection: VerifiedPermissionsOpenIdConnectTokenSelection
    entityIdPrefix: StrictStr | None = None
    groupConfiguration: VerifiedPermissionsOpenIdConnectGroupConfiguration | None = None
