from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaStopCalculationExecutionRequest(BaseModel):
    CalculationExecutionId: StrictStr