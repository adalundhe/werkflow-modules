from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListDataTableAttributesRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    AttributeIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
