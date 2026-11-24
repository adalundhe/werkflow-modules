from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudWatchGetMetricDataQueryDefinitionResponse(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Path: StrictStr | None = None
    Expression: StrictStr | None = None
    Type: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
