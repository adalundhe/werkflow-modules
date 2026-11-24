from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_s3_access_point_vpc_configuration_details import SecurityHubAwsS3AccessPointVpcConfigurationDetails
from .security_hub_aws_s3_account_public_access_block_details import SecurityHubAwsS3AccountPublicAccessBlockDetails


class SecurityHubAwsS3AccessPointDetails(BaseModel):
    AccessPointArn: StrictStr | None = None
    Alias: StrictStr | None = None
    Bucket: StrictStr | None = None
    BucketAccountId: StrictStr | None = None
    Name: StrictStr | None = None
    NetworkOrigin: StrictStr | None = None
    PublicAccessBlockConfiguration: SecurityHubAwsS3AccountPublicAccessBlockDetails | None = None
    VpcConfiguration: SecurityHubAwsS3AccessPointVpcConfigurationDetails | None = None
