from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_in_app_message_content import PinpointInAppMessageContent


class PinpointInAppTemplateResponse(BaseModel):
    Arn: StrictStr | None = None
    Content: list[PinpointInAppMessageContent] | None = None
    CreationDate: StrictStr | None = None
    CustomConfig: dict[StrictStr, StrictStr] | None = None
    LastModifiedDate: StrictStr | None = None
    Layout: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateType: StrictStr | None = None
    Version: StrictStr | None = None
