from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInstanceMetadataServiceConfiguration(BaseModel):
    MinimumInstanceMetadataServiceVersion: StrictStr | None = None
