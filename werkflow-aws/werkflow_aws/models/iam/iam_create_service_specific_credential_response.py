from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_service_specific_credential import IAMServiceSpecificCredential


class IAMCreateServiceSpecificCredentialResponse(BaseModel):
    ServiceSpecificCredential: IAMServiceSpecificCredential | None = None
    ResponseMetadata: dict[str, Any] | None = None
