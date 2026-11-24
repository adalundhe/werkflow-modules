from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_set_refresh_properties import QuickSightDataSetRefreshProperties


class QuickSightPutDataSetRefreshPropertiesRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
    DataSetRefreshProperties: QuickSightDataSetRefreshProperties
