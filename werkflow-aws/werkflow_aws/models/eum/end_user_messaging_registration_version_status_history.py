from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationVersionStatusHistory(BaseModel):
    DraftTimestamp: datetime.datetime | StrictStr | None = None
    SubmittedTimestamp: datetime.datetime | StrictStr | None = None
    AwsReviewingTimestamp: datetime.datetime | StrictStr | None = None
    ReviewingTimestamp: datetime.datetime | StrictStr | None = None
    RequiresAuthenticationTimestamp: datetime.datetime | StrictStr | None = None
    ApprovedTimestamp: datetime.datetime | StrictStr | None = None
    DiscardedTimestamp: datetime.datetime | StrictStr | None = None
    DeniedTimestamp: datetime.datetime | StrictStr | None = None
    RevokedTimestamp: datetime.datetime | StrictStr | None = None
    ArchivedTimestamp: datetime.datetime | StrictStr | None = None
