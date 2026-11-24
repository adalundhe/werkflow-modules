from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2ImageWatermark(BaseModel):
    WatermarkKey: StrictStr | None = None
    SourceImageRegion: StrictStr | None = None
    SourceImageId: StrictStr | None = None
    SourceImageCreationTime: datetime.datetime | StrictStr | None = None
    WatermarkCreationTime: datetime.datetime | StrictStr | None = None
