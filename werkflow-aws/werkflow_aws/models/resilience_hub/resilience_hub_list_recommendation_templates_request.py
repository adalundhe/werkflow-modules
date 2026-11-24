from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ResilienceHubListRecommendationTemplatesRequest(BaseModel):
    assessmentArn: StrictStr | None = None
    maxResults: StrictInt | None = None
    name: StrictStr | None = None
    nextToken: StrictStr | None = None
    recommendationTemplateArn: StrictStr | None = None
    reverseOrder: StrictBool | None = None
    status: list[Literal['Pending', 'InProgress', 'Failed', 'Success']] | None = None
