from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetCalculationExecutionRequest(BaseModel):
    CalculationExecutionId: StrictStr
    