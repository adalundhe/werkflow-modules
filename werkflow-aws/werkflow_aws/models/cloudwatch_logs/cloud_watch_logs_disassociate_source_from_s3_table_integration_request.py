from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDisassociateSourceFromS3TableIntegrationRequest(BaseModel):
    identifier: StrictStr
