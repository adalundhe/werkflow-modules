from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncEvaluateMappingTemplateRequest(BaseModel):
    template: StrictStr
    context: StrictStr
