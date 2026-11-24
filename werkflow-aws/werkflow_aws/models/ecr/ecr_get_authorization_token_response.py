from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_authorization_data import ECRAuthorizationData


class ECRGetAuthorizationTokenResponse(BaseModel):
    authorizationData: list[ECRAuthorizationData] | None = None
    ResponseMetadata: dict[str, Any] | None = None
