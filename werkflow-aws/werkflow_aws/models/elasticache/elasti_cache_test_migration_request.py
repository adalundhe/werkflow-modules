from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_customer_node_endpoint import ElastiCacheCustomerNodeEndpoint


class ElastiCacheTestMigrationRequest(BaseModel):
    ReplicationGroupId: StrictStr
    CustomerNodeEndpointList: list[ElastiCacheCustomerNodeEndpoint]
