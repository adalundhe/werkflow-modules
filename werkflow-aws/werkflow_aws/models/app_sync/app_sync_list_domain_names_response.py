from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_domain_name_config import AppSyncDomainNameConfig


class AppSyncListDomainNamesResponse(BaseModel):
    domainNameConfigs: list[AppSyncDomainNameConfig] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
