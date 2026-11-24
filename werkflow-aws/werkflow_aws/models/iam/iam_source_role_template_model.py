from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMSourceRoleTemplateModel(BaseModel):
    TemplateArn: StrictStr | None = None
    TemplateMinorVersion: StrictInt | None = None
