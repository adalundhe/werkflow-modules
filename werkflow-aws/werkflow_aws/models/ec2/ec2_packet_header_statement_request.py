from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2PacketHeaderStatementRequest(BaseModel):
    SourceAddresses: list[StrictStr] | None = None
    DestinationAddresses: list[StrictStr] | None = None
    SourcePorts: list[StrictStr] | None = None
    DestinationPorts: list[StrictStr] | None = None
    SourcePrefixLists: list[StrictStr] | None = None
    DestinationPrefixLists: list[StrictStr] | None = None
    Protocols: list[Literal['tcp', 'udp']] | None = None
