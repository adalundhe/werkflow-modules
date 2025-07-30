import datetime
from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_calculation_state import AthenaCalculationState

class AthenaCalculationStatus(BaseModel):
    SubmissionDateTime: datetime.datetime
    CompletionDateTime: datetime.datetime
    State: AthenaCalculationState
    StateChangeReason: StrictStr | None = None