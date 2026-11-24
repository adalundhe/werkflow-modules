from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeGuruRepositoryAssociationSummary(BaseModel):
    AssociationArn: StrictStr | None = None
    ConnectionArn: StrictStr | None = None
    LastUpdatedTimeStamp: datetime.datetime | StrictStr | None = None
    AssociationId: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: StrictStr | None = None
    ProviderType: StrictStr | None = None
    State: StrictStr | None = None
