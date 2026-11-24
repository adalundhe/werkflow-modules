from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListContactFlowModuleAliasesRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowModuleId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
