from pydantic import BaseModel, StrictStr, StrictInt, StrictBool


class DescribeCacheClustersRequest(BaseModel):
        CacheClusterId: StrictStr = None,
        MaxRecords: StrictInt = 100,
        Marker: StrictStr | None = None,
        ShowCacheNodeInfo: StrictBool = True,
        ShowCacheClustersNotInReplicationGroups: StrictBool = True,
