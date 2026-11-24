from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_template_version_response import PinpointTemplateVersionResponse


class PinpointTemplateVersionsResponse(BaseModel):
    Item: list[PinpointTemplateVersionResponse] | None = None
    Message: StrictStr | None = None
    NextToken: StrictStr | None = None
    RequestID: StrictStr | None = None
