from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .api_gateway_endpoint_configuration import APIGatewayEndpointConfiguration
from .api_gateway_mutual_tls_authentication_input import APIGatewayMutualTlsAuthenticationInput


class APIGatewayCreateDomainNameRequest(BaseModel):
    domainName: StrictStr
    certificateName: StrictStr | None = None
    certificateBody: StrictStr | None = None
    certificatePrivateKey: StrictStr | None = None
    certificateChain: StrictStr | None = None
    certificateArn: StrictStr | None = None
    regionalCertificateName: StrictStr | None = None
    regionalCertificateArn: StrictStr | None = None
    endpointConfiguration: APIGatewayEndpointConfiguration | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    securityPolicy: Literal['TLS_1_0', 'TLS_1_2', 'SecurityPolicy_TLS13_1_3_2025_09', 'SecurityPolicy_TLS13_1_3_FIPS_2025_09', 'SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_FIPS_PFS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_Ext2_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_Ext2_FIPS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_2021_06', 'SecurityPolicy_TLS13_2025_EDGE', 'SecurityPolicy_TLS12_PFS_2025_EDGE', 'SecurityPolicy_TLS12_2018_EDGE'] | None = None
    endpointAccessMode: Literal['BASIC', 'STRICT'] | None = None
    mutualTlsAuthentication: APIGatewayMutualTlsAuthenticationInput | None = None
    ownershipVerificationCertificateArn: StrictStr | None = None
    policy: StrictStr | None = None
    routingMode: Literal['BASE_PATH_MAPPING_ONLY', 'ROUTING_RULE_ONLY', 'ROUTING_RULE_THEN_BASE_PATH_MAPPING'] | None = None
