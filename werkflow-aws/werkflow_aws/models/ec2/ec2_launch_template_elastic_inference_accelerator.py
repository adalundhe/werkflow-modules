from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplateElasticInferenceAccelerator(BaseModel):
    Type: StrictStr
    Count: StrictInt | None = None
