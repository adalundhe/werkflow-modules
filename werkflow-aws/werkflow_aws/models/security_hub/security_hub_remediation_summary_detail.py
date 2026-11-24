from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_kb_article import SecurityHubKbArticle


class SecurityHubRemediationSummaryDetail(BaseModel):
    Action: StrictStr | None = None
    Description: StrictStr | None = None
    IsImmediate: StrictBool | None = None
    PostRemediationSteps: list[StrictStr] | None = None
    KbArticles: list[SecurityHubKbArticle] | None = None
