from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDeleteGeneratedTemplateRequest(BaseModel):
    GeneratedTemplateName: StrictStr
