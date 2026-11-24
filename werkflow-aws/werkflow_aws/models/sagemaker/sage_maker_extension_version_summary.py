from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerExtensionVersionSummary(BaseModel):
    ExtensionVersion: StrictStr | None = None
