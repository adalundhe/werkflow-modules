from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_o_tel_enrichment_metric_selector import CloudWatchOTelEnrichmentMetricSelector


class CloudWatchUpdateOTelEnrichmentResponse(BaseModel):
    IncludeFilters: list[CloudWatchOTelEnrichmentMetricSelector] | None = None
    ExcludeFilters: list[CloudWatchOTelEnrichmentMetricSelector] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
