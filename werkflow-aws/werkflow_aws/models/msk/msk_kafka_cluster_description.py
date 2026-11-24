from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_amazon_msk_cluster import MSKAmazonMskCluster
from .msk_apache_kafka_cluster import MSKApacheKafkaCluster
from .msk_kafka_cluster_client_authentication import MSKKafkaClusterClientAuthentication
from .msk_kafka_cluster_client_vpc_config import MSKKafkaClusterClientVpcConfig
from .msk_kafka_cluster_encryption_in_transit import MSKKafkaClusterEncryptionInTransit


class MSKKafkaClusterDescription(BaseModel):
    AmazonMskCluster: MSKAmazonMskCluster | None = None
    ApacheKafkaCluster: MSKApacheKafkaCluster | None = None
    KafkaClusterAlias: StrictStr | None = None
    VpcConfig: MSKKafkaClusterClientVpcConfig | None = None
    ClientAuthentication: MSKKafkaClusterClientAuthentication | None = None
    EncryptionInTransit: MSKKafkaClusterEncryptionInTransit | None = None
