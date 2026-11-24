from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_managed_login_branding_type import CognitoIDPManagedLoginBrandingType


class CognitoIDPUpdateManagedLoginBrandingResponse(BaseModel):
    ManagedLoginBranding: CognitoIDPManagedLoginBrandingType | None = None
    ResponseMetadata: dict[str, Any] | None = None
