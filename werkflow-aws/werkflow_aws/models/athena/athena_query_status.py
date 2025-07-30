import datetime
from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_query_error import AthenaQueryError
from .athena_query_state import AthenaQueryState


class AthenaQueryStatus(BaseModel):
    State: AthenaQueryState
    StateChangeReason: StrictStr | None = None
    SubmissionDateTime: datetime.datetime
    CompletionDateTime: datetime.datetime
    AthenaError: AthenaQueryError