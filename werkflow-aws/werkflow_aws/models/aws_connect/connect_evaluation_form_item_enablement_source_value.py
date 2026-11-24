from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class ConnectEvaluationFormItemEnablementSourceValue(BaseModel):
    Type: StrictStr | None = None
    RefId: StrictStr | None = None
    StringValue: StrictStr | None = None
    NumericValue: StrictFloat | StrictInt | None = None
    BooleanValue: StrictBool | None = None
    DateTimeValue: datetime.datetime | StrictStr | None = None
