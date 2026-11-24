from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerResourceSpec(BaseModel):
    SageMakerImageArn: StrictStr | None = None
    SageMakerImageVersionArn: StrictStr | None = None
    SageMakerImageVersionAlias: StrictStr | None = None
    InstanceType: StrictStr | None = None
    LifecycleConfigArn: StrictStr | None = None
    TrainingPlanArn: StrictStr | None = None
