from pydantic import BaseModel, StrictInt, StrictStr


class ElasticacheDescribeReplicationGroupsRequest(BaseModel):
    ReplicationGroupId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
