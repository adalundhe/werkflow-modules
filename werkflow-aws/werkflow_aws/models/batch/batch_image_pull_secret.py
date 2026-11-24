from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchImagePullSecret(BaseModel):
    name: StrictStr | None = None
