from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .msk_replication_starting_position import MSKReplicationStartingPosition
from .msk_replication_topic_name_configuration import MSKReplicationTopicNameConfiguration


class MSKTopicReplication(BaseModel):
    CopyAccessControlListsForTopics: StrictBool | None = None
    CopyTopicConfigurations: StrictBool | None = None
    DetectAndCopyNewTopics: StrictBool | None = None
    StartingPosition: MSKReplicationStartingPosition | None = None
    TopicNameConfiguration: MSKReplicationTopicNameConfiguration | None = None
    TopicsToExclude: list[StrictStr] | None = None
    TopicsToReplicate: list[StrictStr] | None = None
