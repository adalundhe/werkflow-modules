from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ElasticGpuHealth(BaseModel):
    Status: StrictStr | None = None
