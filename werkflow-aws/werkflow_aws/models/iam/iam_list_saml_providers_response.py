from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iamsaml_provider_list_entry import IAMSAMLProviderListEntry


class IAMListSAMLProvidersResponse(BaseModel):
    SAMLProviderList: list[IAMSAMLProviderListEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
