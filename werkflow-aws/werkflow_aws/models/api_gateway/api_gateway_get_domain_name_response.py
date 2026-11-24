from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_endpoint_configuration import APIGatewayEndpointConfiguration
from .api_gateway_mutual_tls_authentication import APIGatewayMutualTlsAuthentication


class APIGatewayGetDomainNameResponse(BaseModel):
    domainName: StrictStr | None = None
    domainNameId: StrictStr | None = None
    domainNameArn: StrictStr | None = None
    certificateName: StrictStr | None = None
    certificateArn: StrictStr | None = None
    certificateUploadDate: datetime.datetime | StrictStr | None = None
    regionalDomainName: StrictStr | None = None
    regionalHostedZoneId: StrictStr | None = None
    regionalCertificateName: StrictStr | None = None
    regionalCertificateArn: StrictStr | None = None
    distributionDomainName: StrictStr | None = None
    distributionHostedZoneId: StrictStr | None = None
    endpointConfiguration: APIGatewayEndpointConfiguration | None = None
    domainNameStatus: StrictStr | None = None
    domainNameStatusMessage: StrictStr | None = None
    securityPolicy: StrictStr | None = None
    endpointAccessMode: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    mutualTlsAuthentication: APIGatewayMutualTlsAuthentication | None = None
    ownershipVerificationCertificateArn: StrictStr | None = None
    managementPolicy: StrictStr | None = None
    policy: StrictStr | None = None
    routingMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
