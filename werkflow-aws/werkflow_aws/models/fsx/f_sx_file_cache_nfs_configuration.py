from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxFileCacheNFSConfiguration(BaseModel):
    Version: Literal['NFS3']
    DnsIps: list[StrictStr] | None = None
