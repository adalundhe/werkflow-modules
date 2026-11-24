from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListTopicsRequest(BaseModel):
    ClusterArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    TopicNameFilter: StrictStr | None = None
