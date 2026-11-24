from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDescribeImageGenerationConfigurationRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
