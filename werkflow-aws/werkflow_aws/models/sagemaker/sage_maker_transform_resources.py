from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerTransformResources(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    TransformAmiVersion: StrictStr | None = None
