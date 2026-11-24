from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateAnalyticsDataSetRequest(BaseModel):
    InstanceId: StrictStr
    DataSetId: StrictStr
    TargetAccountId: StrictStr | None = None
