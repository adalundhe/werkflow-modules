from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_front_staging_distribution_dns_names import CloudFrontStagingDistributionDnsNames
from .cloud_front_traffic_config import CloudFrontTrafficConfig


class CloudFrontContinuousDeploymentPolicyConfig(BaseModel):
    StagingDistributionDnsNames: CloudFrontStagingDistributionDnsNames | None = None
    Enabled: StrictBool | None = None
    TrafficConfig: CloudFrontTrafficConfig | None = None
