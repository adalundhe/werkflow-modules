from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionKinesisDataStream(BaseModel):
    Arn: StrictStr | None = None
