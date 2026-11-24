from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListClusterExtensionsRequest(BaseModel):
    ClusterArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
