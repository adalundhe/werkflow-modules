from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .resilience_hub_s3_location import ResilienceHubS3Location


class ResilienceHubRecommendationTemplate(BaseModel):
    appArn: StrictStr | None = None
    assessmentArn: StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    format: StrictStr | None = None
    message: StrictStr | None = None
    name: StrictStr | None = None
    needsReplacements: StrictBool | None = None
    recommendationIds: list[StrictStr] | None = None
    recommendationTemplateArn: StrictStr | None = None
    recommendationTypes: list[StrictStr] | None = None
    startTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    templatesLocation: ResilienceHubS3Location | None = None
