from pydantic import BaseModel
from .athena_calculation_state import AthenaCalculationState


class AthenaStopCalculationExecutionResponse(BaseModel):
    State: AthenaCalculationState