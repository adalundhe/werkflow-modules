from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ResilienceHubListAppsRequest(BaseModel):
    appArn: StrictStr | None = None
    awsApplicationArn: StrictStr | None = None
    fromLastAssessmentTime: datetime.datetime | StrictStr | None = None
    maxResults: StrictInt | None = None
    name: StrictStr | None = None
    nextToken: StrictStr | None = None
    reverseOrder: StrictBool | None = None
    toLastAssessmentTime: datetime.datetime | StrictStr | None = None
