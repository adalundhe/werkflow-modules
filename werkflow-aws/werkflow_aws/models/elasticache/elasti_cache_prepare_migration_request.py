from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_customer_node_endpoint import ElastiCacheCustomerNodeEndpoint
from .elasti_cache_source_authentication_configuration import ElastiCacheSourceAuthenticationConfiguration
from .elasti_cache_source_tls_configuration import ElastiCacheSourceTlsConfiguration


class ElastiCachePrepareMigrationRequest(BaseModel):
    ServerlessCacheName: StrictStr
    CustomerNodeEndpointList: list[ElastiCacheCustomerNodeEndpoint]
    SourceAuthenticationConfiguration: ElastiCacheSourceAuthenticationConfiguration | None = None
    SourceTlsConfiguration: ElastiCacheSourceTlsConfiguration | None = None
