from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ImageWatermarkFilterResponse(BaseModel):
    WatermarkKey: StrictStr | None = None
    SourceImageRegion: StrictStr | None = None
    MaximumDaysSinceSourceImageCreated: StrictInt | None = None
    MaximumDaysSinceWatermarkCreated: StrictInt | None = None
