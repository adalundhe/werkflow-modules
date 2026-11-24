from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRegisterEventTopicRequest(BaseModel):
    DirectoryId: StrictStr
    TopicName: StrictStr
