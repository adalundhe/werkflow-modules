from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_cognito_group_configuration_item import VerifiedPermissionsCognitoGroupConfigurationItem


class VerifiedPermissionsCognitoUserPoolConfigurationItem(BaseModel):
    userPoolArn: StrictStr | None = None
    clientIds: list[StrictStr] | None = None
    issuer: StrictStr | None = None
    groupConfiguration: VerifiedPermissionsCognitoGroupConfigurationItem | None = None
