from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionVideoMetadata(BaseModel):
    Codec: StrictStr | None = None
    DurationMillis: StrictInt | None = None
    Format: StrictStr | None = None
    FrameRate: StrictFloat | StrictInt | None = None
    FrameHeight: StrictInt | None = None
    FrameWidth: StrictInt | None = None
    ColorRange: StrictStr | None = None
