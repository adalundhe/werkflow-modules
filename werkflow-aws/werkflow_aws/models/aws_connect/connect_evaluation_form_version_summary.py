from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectEvaluationFormVersionSummary(BaseModel):
    EvaluationFormArn: StrictStr | None = None
    EvaluationFormId: StrictStr | None = None
    EvaluationFormVersion: StrictInt | None = None
    Locked: StrictBool | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
