from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_asset_bundle_export_job_summary import QuickSightAssetBundleExportJobSummary


class QuickSightListAssetBundleExportJobsResponse(BaseModel):
    AssetBundleExportJobSummaryList: list[QuickSightAssetBundleExportJobSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
