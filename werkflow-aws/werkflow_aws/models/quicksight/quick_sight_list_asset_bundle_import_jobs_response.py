from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_asset_bundle_import_job_summary import QuickSightAssetBundleImportJobSummary


class QuickSightListAssetBundleImportJobsResponse(BaseModel):
    AssetBundleImportJobSummaryList: list[QuickSightAssetBundleImportJobSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
