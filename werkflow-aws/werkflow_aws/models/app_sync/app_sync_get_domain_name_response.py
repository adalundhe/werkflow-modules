from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_domain_name_config import AppSyncDomainNameConfig


class AppSyncGetDomainNameResponse(BaseModel):
    domainNameConfig: AppSyncDomainNameConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
