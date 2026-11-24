from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2CreateTransitGatewayConnectRequestOptions(BaseModel):
    Protocol: Literal['gre']
