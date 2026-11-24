from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_s3_bucket_website_configuration_redirect_to import SecurityHubAwsS3BucketWebsiteConfigurationRedirectTo
from .security_hub_aws_s3_bucket_website_configuration_routing_rule import SecurityHubAwsS3BucketWebsiteConfigurationRoutingRule


class SecurityHubAwsS3BucketWebsiteConfiguration(BaseModel):
    ErrorDocument: StrictStr | None = None
    IndexDocumentSuffix: StrictStr | None = None
    RedirectAllRequestsTo: SecurityHubAwsS3BucketWebsiteConfigurationRedirectTo | None = None
    RoutingRules: list[SecurityHubAwsS3BucketWebsiteConfigurationRoutingRule] | None = None
