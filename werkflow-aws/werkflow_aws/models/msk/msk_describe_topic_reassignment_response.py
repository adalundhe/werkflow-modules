from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_error_info import MSKErrorInfo


class MSKDescribeTopicReassignmentResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    CompletedTopics: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ErrorInfo: MSKErrorInfo | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    MigratedPartitions: StrictInt | None = None
    Status: StrictStr | None = None
    TargetInstanceType: StrictStr | None = None
    TopicReassignmentOperationArn: StrictStr | None = None
    TopicsToExclude: list[StrictStr] | None = None
    TopicsToInclude: list[StrictStr] | None = None
    TotalPartitions: StrictInt | None = None
    TotalTopics: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
