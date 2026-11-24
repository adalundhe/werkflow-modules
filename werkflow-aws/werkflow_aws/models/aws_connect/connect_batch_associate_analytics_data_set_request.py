from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectBatchAssociateAnalyticsDataSetRequest(BaseModel):
    InstanceId: StrictStr
    DataSetIds: list[StrictStr]
    TargetAccountId: StrictStr | None = None
