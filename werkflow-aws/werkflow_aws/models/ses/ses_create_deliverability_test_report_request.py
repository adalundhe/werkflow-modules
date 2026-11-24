from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_email_content import SESEmailContent
from .ses_tag import SESTag


class SESCreateDeliverabilityTestReportRequest(BaseModel):
    FromEmailAddress: StrictStr
    Content: SESEmailContent
    ReportName: StrictStr | None = None
    Tags: list[SESTag] | None = None
