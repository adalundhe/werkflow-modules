from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_calculation_status import AthenaCalculationStatus
from .athena_calculation_statistics import AthenaCalculationStatistics
from .athena_calculation_result import AthenaCalculationResult


class AthenaGetCalculationExecutionResponse(BaseModel):
    CalculationExecutionId: StrictStr
    SessionId: StrictStr
    Description: StrictStr | None = None
    WorkingDirection: StrictStr
    Status: AthenaCalculationStatus
    Statistics: AthenaCalculationStatistics
    Result: AthenaCalculationResult