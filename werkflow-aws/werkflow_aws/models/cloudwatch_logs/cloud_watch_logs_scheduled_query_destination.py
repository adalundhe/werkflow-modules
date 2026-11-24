from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsScheduledQueryDestination(BaseModel):
    destinationType: StrictStr | None = None
    destinationIdentifier: StrictStr | None = None
    status: StrictStr | None = None
    processedIdentifier: StrictStr | None = None
    errorMessage: StrictStr | None = None
