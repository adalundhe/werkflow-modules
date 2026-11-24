from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDeleteRecommendationTemplateRequest(BaseModel):
    recommendationTemplateArn: StrictStr
    clientToken: StrictStr | None = None
