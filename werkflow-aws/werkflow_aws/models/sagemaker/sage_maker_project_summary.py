from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerProjectSummary(BaseModel):
    ProjectName: StrictStr | None = None
    ProjectDescription: StrictStr | None = None
    ProjectArn: StrictStr | None = None
    ProjectId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ProjectStatus: StrictStr | None = None
