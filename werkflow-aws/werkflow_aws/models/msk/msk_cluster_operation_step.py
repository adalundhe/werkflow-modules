from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_cluster_operation_step_info import MSKClusterOperationStepInfo


class MSKClusterOperationStep(BaseModel):
    StepInfo: MSKClusterOperationStepInfo | None = None
    StepName: StrictStr | None = None
