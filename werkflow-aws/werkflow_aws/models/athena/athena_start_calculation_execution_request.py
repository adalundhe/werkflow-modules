from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_calculation_configuration import AthenaCalculationConfiguration


class AthenaStartCalculationExecutionRequest(BaseModel):
    SessionId: StrictStr
    Description: StrictStr | None = None
    CalculationConfigruation: AthenaCalculationConfiguration | None = None
    CodeBlock: StrictStr | None = None
    ClientRequesttoken: StrictStr | None = None