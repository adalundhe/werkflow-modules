from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ManagedBlockchainListMembersRequest(BaseModel):
    NetworkId: StrictStr
    Name: StrictStr | None = None
    Status: Literal['CREATING', 'AVAILABLE', 'CREATE_FAILED', 'UPDATING', 'DELETING', 'DELETED', 'INACCESSIBLE_ENCRYPTION_KEY'] | None = None
    IsOwned: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
