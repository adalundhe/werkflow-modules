from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectContactFilter(BaseModel):
    ContactStates: list[Literal['INCOMING', 'PENDING', 'CONNECTING', 'CONNECTED', 'CONNECTED_ONHOLD', 'MISSED', 'ERROR', 'ENDED', 'REJECTED']] | None = None
