from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2VCpuInfo(BaseModel):
    DefaultVCpus: StrictInt | None = None
    DefaultCores: StrictInt | None = None
    DefaultThreadsPerCore: StrictInt | None = None
    ValidCores: list[StrictInt] | None = None
    ValidThreadsPerCore: list[StrictInt] | None = None
