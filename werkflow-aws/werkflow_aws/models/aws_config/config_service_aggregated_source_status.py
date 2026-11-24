from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregatedSourceStatus(BaseModel):
    SourceId: StrictStr | None = None
    SourceType: StrictStr | None = None
    AwsRegion: StrictStr | None = None
    LastUpdateStatus: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    LastErrorCode: StrictStr | None = None
    LastErrorMessage: StrictStr | None = None
