from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_kafka_cluster_o_auth_client_credentials import MSKKafkaClusterOAuthClientCredentials
from .msk_kafka_cluster_o_auth_client_credentials_assertion import MSKKafkaClusterOAuthClientCredentialsAssertion
from .msk_kafka_cluster_o_auth_iam_jwt_bearer import MSKKafkaClusterOAuthIamJwtBearer


class MSKKafkaClusterSaslOAuthBearerAuthentication(BaseModel):
    TokenEndpointUrl: StrictStr | None = None
    ClientCredentials: MSKKafkaClusterOAuthClientCredentials | None = None
    IamJwtBearer: MSKKafkaClusterOAuthIamJwtBearer | None = None
    ClientCredentialsAssertion: MSKKafkaClusterOAuthClientCredentialsAssertion | None = None
    TokenEndpointAuthenticationMethod: StrictStr | None = None
    Scope: StrictStr | None = None
    TokenEndpointTlsCertificateArn: StrictStr | None = None
