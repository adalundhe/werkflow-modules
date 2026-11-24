from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_open_id_connect_group_configuration_detail import VerifiedPermissionsOpenIdConnectGroupConfigurationDetail
from .verified_permissions_open_id_connect_token_selection_detail import VerifiedPermissionsOpenIdConnectTokenSelectionDetail


class VerifiedPermissionsOpenIdConnectConfigurationDetail(BaseModel):
    issuer: StrictStr | None = None
    entityIdPrefix: StrictStr | None = None
    groupConfiguration: VerifiedPermissionsOpenIdConnectGroupConfigurationDetail | None = None
    tokenSelection: VerifiedPermissionsOpenIdConnectTokenSelectionDetail | None = None
