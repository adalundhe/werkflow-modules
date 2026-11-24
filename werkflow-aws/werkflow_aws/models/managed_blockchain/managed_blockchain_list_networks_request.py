from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedBlockchainListNetworksRequest(BaseModel):
    Name: StrictStr | None = None
    Framework: Literal['HYPERLEDGER_FABRIC', 'ETHEREUM'] | None = None
    Status: Literal['CREATING', 'AVAILABLE', 'CREATE_FAILED', 'DELETING', 'DELETED'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
