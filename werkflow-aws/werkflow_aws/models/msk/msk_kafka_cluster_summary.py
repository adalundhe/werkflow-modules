from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_amazon_msk_cluster import MSKAmazonMskCluster
from .msk_apache_kafka_cluster import MSKApacheKafkaCluster


class MSKKafkaClusterSummary(BaseModel):
    AmazonMskCluster: MSKAmazonMskCluster | None = None
    ApacheKafkaCluster: MSKApacheKafkaCluster | None = None
    KafkaClusterAlias: StrictStr | None = None
