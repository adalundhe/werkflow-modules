from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyJobConfig(BaseModel):
    buildComputeType: StrictStr | None = None
