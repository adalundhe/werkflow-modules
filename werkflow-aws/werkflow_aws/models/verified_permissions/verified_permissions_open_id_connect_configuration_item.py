from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_open_id_connect_group_configuration_item import VerifiedPermissionsOpenIdConnectGroupConfigurationItem
from .verified_permissions_open_id_connect_token_selection_item import VerifiedPermissionsOpenIdConnectTokenSelectionItem


class VerifiedPermissionsOpenIdConnectConfigurationItem(BaseModel):
    issuer: StrictStr | None = None
    entityIdPrefix: StrictStr | None = None
    groupConfiguration: VerifiedPermissionsOpenIdConnectGroupConfigurationItem | None = None
    tokenSelection: VerifiedPermissionsOpenIdConnectTokenSelectionItem | None = None
