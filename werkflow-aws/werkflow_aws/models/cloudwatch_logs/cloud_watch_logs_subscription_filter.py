from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsSubscriptionFilter(BaseModel):
    filterName: StrictStr | None = None
    logGroupName: StrictStr | None = None
    filterPattern: StrictStr | None = None
    destinationArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    distribution: StrictStr | None = None
    applyOnTransformedLogs: StrictBool | None = None
    creationTime: StrictInt | None = None
    fieldSelectionCriteria: StrictStr | None = None
    emitSystemFields: list[StrictStr] | None = None
