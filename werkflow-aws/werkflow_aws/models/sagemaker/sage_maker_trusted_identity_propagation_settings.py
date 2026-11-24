from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrustedIdentityPropagationSettings(BaseModel):
    Status: StrictStr | None = None
