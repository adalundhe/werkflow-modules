from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_restoration_type import CognitoIDPRestorationType


class CognitoIDPCancelPointInTimeRecoveryResponse(BaseModel):
    Restoration: CognitoIDPRestorationType | None = None
    ResponseMetadata: dict[str, Any] | None = None
