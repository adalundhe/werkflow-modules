from pydantic import BaseModel, StrictStr


class ElasticacheGlobalReplicationGroupInfo(BaseModel):
    GlobalReplicationGroupId: StrictStr
    GlobalReplicationGroupMemberRole: StrictStr