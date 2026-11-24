from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointSMSTemplateRequest(BaseModel):
    Body: StrictStr | None = None
    DefaultSubstitutions: StrictStr | None = None
    RecommenderId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
