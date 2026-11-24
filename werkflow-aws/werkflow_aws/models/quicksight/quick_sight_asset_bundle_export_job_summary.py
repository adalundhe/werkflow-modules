from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightAssetBundleExportJobSummary(BaseModel):
    JobStatus: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    AssetBundleExportJobId: StrictStr | None = None
    IncludeAllDependencies: StrictBool | None = None
    ExportFormat: StrictStr | None = None
    IncludePermissions: StrictBool | None = None
    IncludeTags: StrictBool | None = None
