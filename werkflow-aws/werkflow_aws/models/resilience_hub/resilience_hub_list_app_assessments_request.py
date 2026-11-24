from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ResilienceHubListAppAssessmentsRequest(BaseModel):
    appArn: StrictStr | None = None
    assessmentName: StrictStr | None = None
    assessmentStatus: list[Literal['Pending', 'InProgress', 'Failed', 'Success']] | None = None
    complianceStatus: Literal['PolicyBreached', 'PolicyMet', 'NotApplicable', 'MissingPolicy'] | None = None
    invoker: Literal['User', 'System'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    reverseOrder: StrictBool | None = None
