from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsAmazonMqBrokerUsersDetails(BaseModel):
    PendingChange: StrictStr | None = None
    Username: StrictStr | None = None
