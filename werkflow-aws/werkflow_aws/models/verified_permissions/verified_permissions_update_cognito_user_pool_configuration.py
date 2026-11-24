from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_update_cognito_group_configuration import VerifiedPermissionsUpdateCognitoGroupConfiguration


class VerifiedPermissionsUpdateCognitoUserPoolConfiguration(BaseModel):
    userPoolArn: StrictStr
    clientIds: list[StrictStr] | None = None
    groupConfiguration: VerifiedPermissionsUpdateCognitoGroupConfiguration | None = None
