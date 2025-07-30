from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetCalculationExecutionStatusRequest(BaseModel):
    CalculationExecutionId: StrictStr