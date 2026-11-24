from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDeregisterEventTopicRequest(BaseModel):
    DirectoryId: StrictStr
    TopicName: StrictStr
