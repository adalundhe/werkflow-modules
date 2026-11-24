from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_authorization_data import ECRPublicAuthorizationData


class ECRPublicGetAuthorizationTokenResponse(BaseModel):
    authorizationData: ECRPublicAuthorizationData | None = None
    ResponseMetadata: dict[str, Any] | None = None
