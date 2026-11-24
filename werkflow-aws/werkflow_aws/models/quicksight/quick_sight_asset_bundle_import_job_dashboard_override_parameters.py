from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobDashboardOverrideParameters(BaseModel):
    DashboardId: StrictStr | None = None
    Name: StrictStr | None = None
