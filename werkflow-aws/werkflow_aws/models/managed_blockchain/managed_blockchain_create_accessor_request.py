from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ManagedBlockchainCreateAccessorRequest(BaseModel):
    ClientRequestToken: StrictStr
    AccessorType: Literal['BILLING_TOKEN']
    Tags: dict[StrictStr, StrictStr] | None = None
    NetworkType: Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI'] | None = None
