from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTemplateSourceTemplate(BaseModel):
    Arn: StrictStr
