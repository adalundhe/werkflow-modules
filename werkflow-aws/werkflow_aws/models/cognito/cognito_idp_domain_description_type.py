from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cognito_idp_custom_domain_config_type import CognitoIDPCustomDomainConfigType
from .cognito_idp_routing_type import CognitoIDPRoutingType


class CognitoIDPDomainDescriptionType(BaseModel):
    UserPoolId: StrictStr | None = None
    AWSAccountId: StrictStr | None = None
    Domain: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    CloudFrontDistribution: StrictStr | None = None
    Version: StrictStr | None = None
    Status: StrictStr | None = None
    CustomDomainConfig: CognitoIDPCustomDomainConfigType | None = None
    ManagedLoginVersion: StrictInt | None = None
    Routing: CognitoIDPRoutingType | None = None
