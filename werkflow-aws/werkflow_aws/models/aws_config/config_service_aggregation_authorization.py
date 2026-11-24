from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregationAuthorization(BaseModel):
    AggregationAuthorizationArn: StrictStr | None = None
    AuthorizedAccountId: StrictStr | None = None
    AuthorizedAwsRegion: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
