from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontKinesisStreamConfig(BaseModel):
    RoleARN: StrictStr | None = None
    StreamARN: StrictStr | None = None
