from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointListTemplateVersionsRequest(BaseModel):
    TemplateName: StrictStr
    TemplateType: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
