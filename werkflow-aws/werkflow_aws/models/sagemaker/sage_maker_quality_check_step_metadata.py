from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerQualityCheckStepMetadata(BaseModel):
    CheckType: StrictStr | None = None
    BaselineUsedForDriftCheckStatistics: StrictStr | None = None
    BaselineUsedForDriftCheckConstraints: StrictStr | None = None
    CalculatedBaselineStatistics: StrictStr | None = None
    CalculatedBaselineConstraints: StrictStr | None = None
    ModelPackageGroupName: StrictStr | None = None
    ViolationReport: StrictStr | None = None
    CheckJobArn: StrictStr | None = None
    SkipCheck: StrictBool | None = None
    RegisterNewBaseline: StrictBool | None = None
