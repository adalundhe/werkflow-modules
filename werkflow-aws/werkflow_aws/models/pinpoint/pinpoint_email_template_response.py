from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_message_header import PinpointMessageHeader


class PinpointEmailTemplateResponse(BaseModel):
    Arn: StrictStr | None = None
    CreationDate: StrictStr | None = None
    DefaultSubstitutions: StrictStr | None = None
    HtmlPart: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    RecommenderId: StrictStr | None = None
    Subject: StrictStr | None = None
    Headers: list[PinpointMessageHeader] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateType: StrictStr | None = None
    TextPart: StrictStr | None = None
    Version: StrictStr | None = None
