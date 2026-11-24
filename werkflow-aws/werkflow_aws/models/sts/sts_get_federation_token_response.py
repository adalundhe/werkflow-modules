from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .sts_credentials import STSCredentials
from .sts_federated_user import STSFederatedUser


class STSGetFederationTokenResponse(BaseModel):
    Credentials: STSCredentials | None = None
    FederatedUser: STSFederatedUser | None = None
    PackedPolicySize: StrictInt | None = None
    SessionTokenUtilization: StrictInt | None = None
    SessionTokenSize: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
