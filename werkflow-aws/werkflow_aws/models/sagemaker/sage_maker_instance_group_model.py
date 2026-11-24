from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerInstanceGroupModel(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    InstanceGroupName: StrictStr | None = None
