from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_user_data_filters import ConnectUserDataFilters


class ConnectGetCurrentUserDataRequest(BaseModel):
    InstanceId: StrictStr
    Filters: ConnectUserDataFilters
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
