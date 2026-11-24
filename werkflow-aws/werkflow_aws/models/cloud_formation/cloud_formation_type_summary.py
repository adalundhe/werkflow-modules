from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationTypeSummary(BaseModel):
    Type: StrictStr | None = None
    TypeName: StrictStr | None = None
    DefaultVersionId: StrictStr | None = None
    TypeArn: StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    PublisherId: StrictStr | None = None
    OriginalTypeName: StrictStr | None = None
    PublicVersionNumber: StrictStr | None = None
    LatestPublicVersion: StrictStr | None = None
    PublisherIdentity: StrictStr | None = None
    PublisherName: StrictStr | None = None
    IsActivated: StrictBool | None = None
