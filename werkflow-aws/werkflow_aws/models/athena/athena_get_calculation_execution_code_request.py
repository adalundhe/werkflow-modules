from pydantic import BaseModel, StrictStr


class AthenaGetCalculationExecutionCodeRequest(BaseModel):
    CalculationExecutionId: StrictStr


AthenaGetCalculationExectutionCodeRequest = AthenaGetCalculationExecutionCodeRequest
