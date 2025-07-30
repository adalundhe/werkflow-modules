from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_calculation_state import AthenaCalculationState


class AthenaStartCalculationExecutionResponse(BaseModel):
    CalculationExecutionId: StrictStr
    State: AthenaCalculationState