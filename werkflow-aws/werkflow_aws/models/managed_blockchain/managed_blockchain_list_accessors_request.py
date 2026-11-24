from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ManagedBlockchainListAccessorsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    NetworkType: Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI'] | None = None
