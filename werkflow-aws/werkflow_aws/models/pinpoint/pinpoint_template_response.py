from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointTemplateResponse(BaseModel):
    Arn: StrictStr | None = None
    CreationDate: StrictStr | None = None
    DefaultSubstitutions: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateType: StrictStr | None = None
    Version: StrictStr | None = None
