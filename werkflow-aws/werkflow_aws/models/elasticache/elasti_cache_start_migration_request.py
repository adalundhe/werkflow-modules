from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_customer_node_endpoint import ElastiCacheCustomerNodeEndpoint


class ElastiCacheStartMigrationRequest(BaseModel):
    ServerlessCacheName: StrictStr | None = None
    ReplicationGroupId: StrictStr | None = None
    CustomerNodeEndpointList: list[ElastiCacheCustomerNodeEndpoint] | None = None
    AutoCutover: StrictBool | None = None
    ClearTargetCacheData: StrictBool | None = None
