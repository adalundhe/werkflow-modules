from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_calculation_status import AthenaCalculationStatus
from .athena_calculation_statistics import AthenaCalculationStatistics
from .athena_calculation_result import AthenaCalculationResult


class AthenaGetCalculationExecutionResponse(BaseModel):
    CalculationExecutionId: StrictStr | None = None
    SessionId: StrictStr | None = None
    Description: StrictStr | None = None
    WorkingDirectory: StrictStr | None = None
    Status: AthenaCalculationStatus | None = None
    Statistics: AthenaCalculationStatistics | None = None
    Result: AthenaCalculationResult | None = None
