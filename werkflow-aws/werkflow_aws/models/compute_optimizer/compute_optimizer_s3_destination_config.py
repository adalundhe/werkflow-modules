from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerS3DestinationConfig(BaseModel):
    bucket: StrictStr | None = None
    keyPrefix: StrictStr | None = None
