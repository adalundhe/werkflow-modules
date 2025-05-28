from pydantic import BaseModel, StrictStr, StrictInt


class ElasticacheDescribeReplicationGroupsRequest(BaseModel):
        ReplicationGroupId: StrictStr = None
        MaxRecords: StrictInt = 100
        Marker: StrictStr | None = None
