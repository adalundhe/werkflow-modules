from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_notify_template_filter import EndUserMessagingNotifyTemplateFilter


class EndUserMessagingDescribeNotifyTemplatesRequest(BaseModel):
    TemplateIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingNotifyTemplateFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
