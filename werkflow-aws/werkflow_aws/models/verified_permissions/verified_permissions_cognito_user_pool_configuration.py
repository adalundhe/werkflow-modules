from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_cognito_group_configuration import VerifiedPermissionsCognitoGroupConfiguration


class VerifiedPermissionsCognitoUserPoolConfiguration(BaseModel):
    userPoolArn: StrictStr
    clientIds: list[StrictStr] | None = None
    groupConfiguration: VerifiedPermissionsCognitoGroupConfiguration | None = None
