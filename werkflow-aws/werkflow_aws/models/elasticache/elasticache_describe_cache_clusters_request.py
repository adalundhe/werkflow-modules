from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElasticacheDescribeCacheClustersRequest(BaseModel):
    CacheClusterId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    ShowCacheNodeInfo: StrictBool | None = None
    ShowCacheClustersNotInReplicationGroups: StrictBool | None = None
