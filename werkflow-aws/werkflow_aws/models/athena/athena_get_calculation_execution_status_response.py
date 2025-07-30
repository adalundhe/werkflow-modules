from pydantic import BaseModel
from .athena_calculation_status import AthenaCalculationStatus
from .athena_calculation_statistics import AthenaCalculationStatistics


class AthenaGetCalculationExecutionStatusResponse(BaseModel):
    Status: AthenaCalculationStatus
    Statistics: AthenaCalculationStatistics