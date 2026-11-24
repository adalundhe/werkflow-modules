from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SageMakerClusterNetworkInterface(BaseModel):
    InterfaceType: Literal['efa', 'efa-only'] | None = None
