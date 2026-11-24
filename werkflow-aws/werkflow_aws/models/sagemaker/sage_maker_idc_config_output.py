from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerIdcConfigOutput(BaseModel):
    InstanceArn: StrictStr | None = None
    ApplicationArn: StrictStr | None = None
