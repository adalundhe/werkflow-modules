from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionKinesisVideoStream(BaseModel):
    Arn: StrictStr | None = None
