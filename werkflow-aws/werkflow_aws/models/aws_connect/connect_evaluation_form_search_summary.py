from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectEvaluationFormSearchSummary(BaseModel):
    EvaluationFormId: StrictStr | None = None
    EvaluationFormArn: StrictStr | None = None
    Title: StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
    LastActivatedTime: datetime.datetime | StrictStr | None = None
    LastActivatedBy: StrictStr | None = None
    LatestVersion: StrictInt | None = None
    ActiveVersion: StrictInt | None = None
    AutoEvaluationEnabled: StrictBool | None = None
    EvaluationFormLanguage: StrictStr | None = None
    ContactInteractionType: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    AIVersion: StrictStr | None = None
