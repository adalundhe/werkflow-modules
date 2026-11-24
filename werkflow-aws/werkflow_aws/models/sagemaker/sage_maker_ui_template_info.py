from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUiTemplateInfo(BaseModel):
    Url: StrictStr | None = None
    ContentSha256: StrictStr | None = None
