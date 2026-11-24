from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerIdcConfigInput(BaseModel):
    InstanceArn: StrictStr
