from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceEventTopic(BaseModel):
    DirectoryId: StrictStr | None = None
    TopicName: StrictStr | None = None
    TopicArn: StrictStr | None = None
    CreatedDateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
