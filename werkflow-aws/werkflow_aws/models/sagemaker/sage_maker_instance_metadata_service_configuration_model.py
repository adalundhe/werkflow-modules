from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInstanceMetadataServiceConfigurationModel(BaseModel):
    MinimumInstanceMetadataServiceVersion: StrictStr | None = None
