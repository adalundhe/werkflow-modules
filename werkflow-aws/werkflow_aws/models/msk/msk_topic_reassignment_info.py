from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class MSKTopicReassignmentInfo(BaseModel):
    CompletedTopics: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    TargetInstanceType: StrictStr | None = None
    TopicReassignmentOperationArn: StrictStr | None = None
    TotalTopics: StrictInt | None = None
