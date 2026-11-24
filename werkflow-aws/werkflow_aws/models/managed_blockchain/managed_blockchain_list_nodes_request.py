from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedBlockchainListNodesRequest(BaseModel):
    NetworkId: StrictStr
    MemberId: StrictStr | None = None
    Status: Literal['CREATING', 'AVAILABLE', 'UNHEALTHY', 'CREATE_FAILED', 'UPDATING', 'DELETING', 'DELETED', 'FAILED', 'INACCESSIBLE_ENCRYPTION_KEY'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
