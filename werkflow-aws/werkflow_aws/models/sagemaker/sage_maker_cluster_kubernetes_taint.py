from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterKubernetesTaint(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    Effect: StrictStr | None = None
