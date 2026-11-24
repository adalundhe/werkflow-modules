from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsJSONMappingParameters(BaseModel):
    RecordRowPath: StrictStr | None = None
