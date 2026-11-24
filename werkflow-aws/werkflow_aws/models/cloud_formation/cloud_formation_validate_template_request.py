from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationValidateTemplateRequest(BaseModel):
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
