from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2HostCpuOptions(BaseModel):
    AmdSevSnp: StrictStr | None = None
