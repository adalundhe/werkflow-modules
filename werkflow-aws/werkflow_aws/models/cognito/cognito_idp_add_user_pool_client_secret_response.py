from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_client_secret_descriptor_type import CognitoIDPClientSecretDescriptorType


class CognitoIDPAddUserPoolClientSecretResponse(BaseModel):
    ClientSecretDescriptor: CognitoIDPClientSecretDescriptorType | None = None
    ResponseMetadata: dict[str, Any] | None = None
