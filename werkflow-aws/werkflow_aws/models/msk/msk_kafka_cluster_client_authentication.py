from __future__ import annotations
from pydantic import BaseModel
from .msk_kafka_cluster_mtls_authentication import MSKKafkaClusterMTLSAuthentication
from .msk_kafka_cluster_sasl_o_auth_bearer_authentication import MSKKafkaClusterSaslOAuthBearerAuthentication
from .msk_kafka_cluster_sasl_scram_authentication import MSKKafkaClusterSaslScramAuthentication


class MSKKafkaClusterClientAuthentication(BaseModel):
    SaslScram: MSKKafkaClusterSaslScramAuthentication | None = None
    MTLS: MSKKafkaClusterMTLSAuthentication | None = None
    SaslOAuthBearer: MSKKafkaClusterSaslOAuthBearerAuthentication | None = None
