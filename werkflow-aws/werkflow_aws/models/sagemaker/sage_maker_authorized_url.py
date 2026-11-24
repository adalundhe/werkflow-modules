from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAuthorizedUrl(BaseModel):
    Url: StrictStr | None = None
    LocalPath: StrictStr | None = None
