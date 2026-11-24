from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMGetRoleTemplateVersionRequest(BaseModel):
    TemplateArn: StrictStr
    MinorVersion: StrictInt | None = None
