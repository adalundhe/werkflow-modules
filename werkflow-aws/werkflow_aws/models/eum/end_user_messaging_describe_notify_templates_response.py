from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_notify_template_information import EndUserMessagingNotifyTemplateInformation


class EndUserMessagingDescribeNotifyTemplatesResponse(BaseModel):
    NotifyTemplates: list[EndUserMessagingNotifyTemplateInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
