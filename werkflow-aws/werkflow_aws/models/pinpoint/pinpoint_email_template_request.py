from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_message_header import PinpointMessageHeader


class PinpointEmailTemplateRequest(BaseModel):
    DefaultSubstitutions: StrictStr | None = None
    HtmlPart: StrictStr | None = None
    RecommenderId: StrictStr | None = None
    Subject: StrictStr | None = None
    Headers: list[PinpointMessageHeader] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
    TextPart: StrictStr | None = None
