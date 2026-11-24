from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListUseCasesRequest(BaseModel):
    InstanceId: StrictStr
    IntegrationAssociationId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
