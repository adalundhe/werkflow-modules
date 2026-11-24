from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerS3Destination(BaseModel):
    bucket: StrictStr | None = None
    key: StrictStr | None = None
    metadataKey: StrictStr | None = None
