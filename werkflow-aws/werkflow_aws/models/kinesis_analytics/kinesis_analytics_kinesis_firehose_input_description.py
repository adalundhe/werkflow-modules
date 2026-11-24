from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsKinesisFirehoseInputDescription(BaseModel):
    ResourceARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
