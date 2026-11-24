from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchNetworkConfiguration(BaseModel):
    assignPublicIp: StrictStr | None = None
