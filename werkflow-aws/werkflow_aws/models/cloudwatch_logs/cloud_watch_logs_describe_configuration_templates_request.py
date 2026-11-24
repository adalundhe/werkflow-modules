from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeConfigurationTemplatesRequest(BaseModel):
    service: StrictStr | None = None
    logTypes: list[StrictStr] | None = None
    resourceTypes: list[StrictStr] | None = None
    deliveryDestinationTypes: list[Literal['S3', 'CWL', 'FH', 'XRAY']] | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
