from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerLineageGroupSummary(BaseModel):
    LineageGroupArn: StrictStr | None = None
    LineageGroupName: StrictStr | None = None
    DisplayName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
