from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetCalculationExectutionCodeRequest(BaseModel):
    CalculationExecutionId: StrictStr