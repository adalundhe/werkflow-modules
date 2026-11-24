from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2HostCpuOptionsRequest(BaseModel):
    AmdSevSnp: Literal['enabled', 'disabled'] | None = None
