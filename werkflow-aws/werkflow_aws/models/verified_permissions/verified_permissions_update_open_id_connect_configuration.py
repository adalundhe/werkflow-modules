from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_update_open_id_connect_group_configuration import VerifiedPermissionsUpdateOpenIdConnectGroupConfiguration
from .verified_permissions_update_open_id_connect_token_selection import VerifiedPermissionsUpdateOpenIdConnectTokenSelection


class VerifiedPermissionsUpdateOpenIdConnectConfiguration(BaseModel):
    issuer: StrictStr
    tokenSelection: VerifiedPermissionsUpdateOpenIdConnectTokenSelection
    entityIdPrefix: StrictStr | None = None
    groupConfiguration: VerifiedPermissionsUpdateOpenIdConnectGroupConfiguration | None = None
