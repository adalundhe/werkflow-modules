from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_open_id_connect_provider_list_entry import IAMOpenIDConnectProviderListEntry


class IAMListOpenIDConnectProvidersResponse(BaseModel):
    OpenIDConnectProviderList: list[IAMOpenIDConnectProviderListEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
