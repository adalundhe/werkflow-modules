from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsAmazonMqBrokerLogsPendingDetails(BaseModel):
    Audit: StrictBool | None = None
    General: StrictBool | None = None
