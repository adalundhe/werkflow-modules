from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMSourceRoleTemplate(BaseModel):
    TemplateArn: StrictStr | None = None
    TemplateMinorVersion: StrictInt | None = None
