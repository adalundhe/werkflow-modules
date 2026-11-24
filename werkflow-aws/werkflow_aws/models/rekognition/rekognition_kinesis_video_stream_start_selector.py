from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionKinesisVideoStreamStartSelector(BaseModel):
    ProducerTimestamp: StrictInt | None = None
    FragmentNumber: StrictStr | None = None
