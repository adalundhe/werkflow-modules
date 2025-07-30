from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaGetCalculationExecutionCodeResponse(BaseModel):
    CodeBlock: StrictStr