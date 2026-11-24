from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplateElasticInferenceAcceleratorResponse(BaseModel):
    Type: StrictStr | None = None
    Count: StrictInt | None = None
