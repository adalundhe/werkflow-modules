from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_o_tel_enrichment_metric_selector import CloudWatchOTelEnrichmentMetricSelector


class CloudWatchStartOTelEnrichmentRequest(BaseModel):
    IncludeFilters: list[CloudWatchOTelEnrichmentMetricSelector] | None = None
    ExcludeFilters: list[CloudWatchOTelEnrichmentMetricSelector] | None = None
