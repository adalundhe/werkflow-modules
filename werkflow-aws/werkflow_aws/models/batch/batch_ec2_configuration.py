from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEc2Configuration(BaseModel):
    imageType: StrictStr | None = None
    imageIdOverride: StrictStr | None = None
    batchImageStatus: StrictStr | None = None
    imageKubernetesVersion: StrictStr | None = None
