from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ecr_repository_image_scanning_configuration_details import SecurityHubAwsEcrRepositoryImageScanningConfigurationDetails
from .security_hub_aws_ecr_repository_lifecycle_policy_details import SecurityHubAwsEcrRepositoryLifecyclePolicyDetails


class SecurityHubAwsEcrRepositoryDetails(BaseModel):
    Arn: StrictStr | None = None
    ImageScanningConfiguration: SecurityHubAwsEcrRepositoryImageScanningConfigurationDetails | None = None
    ImageTagMutability: StrictStr | None = None
    LifecyclePolicy: SecurityHubAwsEcrRepositoryLifecyclePolicyDetails | None = None
    RepositoryName: StrictStr | None = None
    RepositoryPolicyText: StrictStr | None = None
