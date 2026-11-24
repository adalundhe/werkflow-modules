from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateAnalyticsDataSetRequest(BaseModel):
    InstanceId: StrictStr
    DataSetId: StrictStr
    TargetAccountId: StrictStr | None = None
