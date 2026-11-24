from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_code_delivery_details_type import CognitoIDPCodeDeliveryDetailsType


class CognitoIDPGetUserAttributeVerificationCodeResponse(BaseModel):
    CodeDeliveryDetails: CognitoIDPCodeDeliveryDetailsType | None = None
    ResponseMetadata: dict[str, Any] | None = None
