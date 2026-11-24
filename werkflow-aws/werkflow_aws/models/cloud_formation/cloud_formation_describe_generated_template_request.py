from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeGeneratedTemplateRequest(BaseModel):
    GeneratedTemplateName: StrictStr
