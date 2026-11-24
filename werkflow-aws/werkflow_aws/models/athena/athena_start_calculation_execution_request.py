from pydantic import BaseModel, StrictStr
from .athena_calculation_configuration import AthenaCalculationConfiguration


class AthenaStartCalculationExecutionRequest(BaseModel):
    SessionId: StrictStr
    Description: StrictStr | None = None
    CalculationConfiguration: AthenaCalculationConfiguration | None = None
    CodeBlock: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
