from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobSummary(BaseModel):
    JobStatus: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    AssetBundleImportJobId: StrictStr | None = None
    FailureAction: StrictStr | None = None
