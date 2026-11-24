from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_template_response import PinpointTemplateResponse


class PinpointTemplatesResponse(BaseModel):
    Item: list[PinpointTemplateResponse] | None = None
    NextToken: StrictStr | None = None
