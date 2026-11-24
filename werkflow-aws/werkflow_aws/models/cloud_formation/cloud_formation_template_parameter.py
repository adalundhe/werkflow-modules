from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationTemplateParameter(BaseModel):
    ParameterKey: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    NoEcho: StrictBool | None = None
    Description: StrictStr | None = None
