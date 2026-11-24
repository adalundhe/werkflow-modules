from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKTopicReplicationUpdate(BaseModel):
    CopyAccessControlListsForTopics: StrictBool
    CopyTopicConfigurations: StrictBool
    DetectAndCopyNewTopics: StrictBool
    TopicsToExclude: list[StrictStr]
    TopicsToReplicate: list[StrictStr]
