from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockS3DataSource(BaseModel):
    s3Uri: StrictStr | None = None
