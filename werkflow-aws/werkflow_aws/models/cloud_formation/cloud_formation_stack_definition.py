from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationStackDefinition(BaseModel):
    StackName: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    TemplateURL: StrictStr | None = None
