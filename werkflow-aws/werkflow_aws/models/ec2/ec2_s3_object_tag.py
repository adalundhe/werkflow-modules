from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2S3ObjectTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
