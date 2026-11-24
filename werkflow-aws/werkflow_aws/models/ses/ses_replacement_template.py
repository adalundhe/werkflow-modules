from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESReplacementTemplate(BaseModel):
    ReplacementTemplateData: StrictStr | None = None
