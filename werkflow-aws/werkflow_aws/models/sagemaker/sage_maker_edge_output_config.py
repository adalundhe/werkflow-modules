from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEdgeOutputConfig(BaseModel):
    S3OutputLocation: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    PresetDeploymentType: StrictStr | None = None
    PresetDeploymentConfig: StrictStr | None = None
