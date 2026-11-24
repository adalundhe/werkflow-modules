from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_status import OpenSearchDomainStatus
from .open_search_dry_run_progress_status import OpenSearchDryRunProgressStatus
from .open_search_dry_run_results import OpenSearchDryRunResults


class OpenSearchDescribeDryRunProgressResponse(BaseModel):
    DryRunProgressStatus: OpenSearchDryRunProgressStatus | None = None
    DryRunConfig: OpenSearchDomainStatus | None = None
    DryRunResults: OpenSearchDryRunResults | None = None
    ResponseMetadata: dict[str, Any] | None = None
