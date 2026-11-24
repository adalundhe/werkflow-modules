from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudWatchMetricStreamEntry(BaseModel):
    Arn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastUpdateDate: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    FirehoseArn: StrictStr | None = None
    State: StrictStr | None = None
    OutputFormat: StrictStr | None = None
