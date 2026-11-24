from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectEvaluationFormSummary(BaseModel):
    EvaluationFormId: StrictStr | None = None
    EvaluationFormArn: StrictStr | None = None
    Title: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
    LastActivatedTime: datetime.datetime | StrictStr | None = None
    LastActivatedBy: StrictStr | None = None
    LatestVersion: StrictInt | None = None
    ActiveVersion: StrictInt | None = None
