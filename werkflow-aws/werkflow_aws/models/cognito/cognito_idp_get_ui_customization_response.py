from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idpui_customization_type import CognitoIDPUICustomizationType


class CognitoIDPGetUICustomizationResponse(BaseModel):
    UICustomization: CognitoIDPUICustomizationType | None = None
    ResponseMetadata: dict[str, Any] | None = None
