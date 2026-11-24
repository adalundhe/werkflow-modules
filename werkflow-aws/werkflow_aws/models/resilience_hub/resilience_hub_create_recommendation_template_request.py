from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ResilienceHubCreateRecommendationTemplateRequest(BaseModel):
    assessmentArn: StrictStr
    name: StrictStr
    bucketName: StrictStr | None = None
    clientToken: StrictStr | None = None
    format: Literal['CfnYaml', 'CfnJson'] | None = None
    recommendationIds: list[StrictStr] | None = None
    recommendationTypes: list[Literal['Alarm', 'Sop', 'Test']] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
