from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsPutSubscriptionFilterRequest(BaseModel):
    logGroupName: StrictStr
    filterName: StrictStr
    filterPattern: StrictStr
    destinationArn: StrictStr
    roleArn: StrictStr | None = None
    distribution: Literal['Random', 'ByLogStream'] | None = None
    applyOnTransformedLogs: StrictBool | None = None
    fieldSelectionCriteria: StrictStr | None = None
    emitSystemFields: list[StrictStr] | None = None
