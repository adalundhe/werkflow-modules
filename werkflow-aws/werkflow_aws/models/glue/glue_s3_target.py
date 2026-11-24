from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueS3Target(BaseModel):
    Path: StrictStr | None = None
    Exclusions: list[StrictStr] | None = None
    ConnectionName: StrictStr | None = None
    SampleSize: StrictInt | None = None
    EventQueueArn: StrictStr | None = None
    DlqEventQueueArn: StrictStr | None = None
