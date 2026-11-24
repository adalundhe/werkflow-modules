from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class ConnectEvaluationAnswerData(BaseModel):
    StringValue: StrictStr | None = None
    NumericValue: StrictFloat | StrictInt | None = None
    StringValues: list[StrictStr] | None = None
    DateTimeValue: StrictStr | None = None
    NotApplicable: StrictBool | None = None
