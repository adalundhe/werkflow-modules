from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKDescribeTopicPartitionsRequest(BaseModel):
    ClusterArn: StrictStr
    TopicName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
