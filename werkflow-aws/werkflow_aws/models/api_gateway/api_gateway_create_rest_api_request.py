from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .api_gateway_endpoint_configuration import APIGatewayEndpointConfiguration


class APIGatewayCreateRestApiRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
    version: StrictStr | None = None
    cloneFrom: StrictStr | None = None
    binaryMediaTypes: list[StrictStr] | None = None
    minimumCompressionSize: StrictInt | None = None
    apiKeySource: Literal['HEADER', 'AUTHORIZER'] | None = None
    endpointConfiguration: APIGatewayEndpointConfiguration | None = None
    policy: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    disableExecuteApiEndpoint: StrictBool | None = None
    securityPolicy: Literal['TLS_1_0', 'TLS_1_2', 'SecurityPolicy_TLS13_1_3_2025_09', 'SecurityPolicy_TLS13_1_3_FIPS_2025_09', 'SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_FIPS_PFS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_Ext2_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_Ext2_FIPS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_2021_06', 'SecurityPolicy_TLS13_2025_EDGE', 'SecurityPolicy_TLS12_PFS_2025_EDGE', 'SecurityPolicy_TLS12_2018_EDGE'] | None = None
    endpointAccessMode: Literal['BASIC', 'STRICT'] | None = None
