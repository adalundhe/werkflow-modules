from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ManagedBlockchainNetworkFabricConfiguration(BaseModel):
    Edition: Literal['STARTER', 'STANDARD']
