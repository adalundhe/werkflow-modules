from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_config import OpenSearchDomainConfig
from .open_search_dry_run_progress_status import OpenSearchDryRunProgressStatus
from .open_search_dry_run_results import OpenSearchDryRunResults


class OpenSearchUpdateDomainConfigResponse(BaseModel):
    DomainConfig: OpenSearchDomainConfig | None = None
    DryRunResults: OpenSearchDryRunResults | None = None
    DryRunProgressStatus: OpenSearchDryRunProgressStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
