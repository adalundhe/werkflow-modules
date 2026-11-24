from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2VpcBlockPublicAccessOptions(BaseModel):
    AwsAccountId: StrictStr | None = None
    AwsRegion: StrictStr | None = None
    State: StrictStr | None = None
    InternetGatewayBlockMode: StrictStr | None = None
    Reason: StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    ManagedBy: StrictStr | None = None
    ExclusionsAllowed: StrictStr | None = None
