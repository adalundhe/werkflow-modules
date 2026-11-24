from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightTemplateAlias(BaseModel):
    AliasName: StrictStr | None = None
    Arn: StrictStr | None = None
    TemplateVersionNumber: StrictInt | None = None
