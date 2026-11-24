from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_environment_parameter import SageMakerEnvironmentParameter


class SageMakerModelConfiguration(BaseModel):
    InferenceSpecificationName: StrictStr | None = None
    EnvironmentParameters: list[SageMakerEnvironmentParameter] | None = None
    CompilationJobName: StrictStr | None = None
