from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_client_secret_descriptor_type import CognitoIDPClientSecretDescriptorType


class CognitoIDPListUserPoolClientSecretsResponse(BaseModel):
    ClientSecrets: list[CognitoIDPClientSecretDescriptorType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
