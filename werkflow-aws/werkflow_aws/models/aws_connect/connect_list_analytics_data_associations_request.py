from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListAnalyticsDataAssociationsRequest(BaseModel):
    InstanceId: StrictStr
    DataSetId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
