from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointListTemplatesRequest(BaseModel):
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
    Prefix: StrictStr | None = None
    TemplateType: StrictStr | None = None
