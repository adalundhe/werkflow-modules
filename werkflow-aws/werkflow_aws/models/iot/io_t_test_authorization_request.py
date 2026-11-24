from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_auth_info import IoTAuthInfo


class IoTTestAuthorizationRequest(BaseModel):
    authInfos: list[IoTAuthInfo]
    principal: StrictStr | None = None
    cognitoIdentityPoolId: StrictStr | None = None
    clientId: StrictStr | None = None
    policyNamesToAdd: list[StrictStr] | None = None
    policyNamesToSkip: list[StrictStr] | None = None
