from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_account_settings_detail import OpenSearchServerlessAccountSettingsDetail


class OpenSearchServerlessGetAccountSettingsResponse(BaseModel):
    accountSettingsDetail: OpenSearchServerlessAccountSettingsDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
