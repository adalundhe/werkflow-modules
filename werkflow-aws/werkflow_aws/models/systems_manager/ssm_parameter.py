from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SSMParameter(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Value: StrictStr | None = None
    Version: StrictInt | None = None
    Selector: StrictStr | None = None
    SourceResult: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    ARN: StrictStr | None = None
    DataType: StrictStr | None = None
