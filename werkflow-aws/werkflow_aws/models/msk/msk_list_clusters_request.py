# response = client.list_clusters(
#     ClusterNameFilter='string',
#     MaxResults=123,
#     NextToken='string'
# )

from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class MSKListClustersRequest(BaseModel):
    ClusterNameFilter: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None