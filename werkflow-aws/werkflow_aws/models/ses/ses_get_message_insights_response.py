from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_email_insights import SESEmailInsights
from .ses_message_tag import SESMessageTag


class SESGetMessageInsightsResponse(BaseModel):
    MessageId: StrictStr | None = None
    FromEmailAddress: StrictStr | None = None
    Subject: StrictStr | None = None
    EmailTags: list[SESMessageTag] | None = None
    Insights: list[SESEmailInsights] | None = None
    ResponseMetadata: dict[str, Any] | None = None
