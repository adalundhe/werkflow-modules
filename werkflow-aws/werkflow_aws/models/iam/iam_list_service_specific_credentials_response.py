from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_service_specific_credential_metadata import IAMServiceSpecificCredentialMetadata


class IAMListServiceSpecificCredentialsResponse(BaseModel):
    ServiceSpecificCredentials: list[IAMServiceSpecificCredentialMetadata] | None = None
    Marker: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
