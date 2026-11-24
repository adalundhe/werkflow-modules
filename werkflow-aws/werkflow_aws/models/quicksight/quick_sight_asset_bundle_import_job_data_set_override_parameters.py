from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_refresh_properties import QuickSightDataSetRefreshProperties


class QuickSightAssetBundleImportJobDataSetOverrideParameters(BaseModel):
    DataSetId: StrictStr | None = None
    Name: StrictStr | None = None
    DataSetRefreshProperties: QuickSightDataSetRefreshProperties | None = None
