from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_elastic_beanstalk_environment_environment_link import SecurityHubAwsElasticBeanstalkEnvironmentEnvironmentLink
from .security_hub_aws_elastic_beanstalk_environment_option_setting import SecurityHubAwsElasticBeanstalkEnvironmentOptionSetting
from .security_hub_aws_elastic_beanstalk_environment_tier import SecurityHubAwsElasticBeanstalkEnvironmentTier


class SecurityHubAwsElasticBeanstalkEnvironmentDetails(BaseModel):
    ApplicationName: StrictStr | None = None
    Cname: StrictStr | None = None
    DateCreated: StrictStr | None = None
    DateUpdated: StrictStr | None = None
    Description: StrictStr | None = None
    EndpointUrl: StrictStr | None = None
    EnvironmentArn: StrictStr | None = None
    EnvironmentId: StrictStr | None = None
    EnvironmentLinks: list[SecurityHubAwsElasticBeanstalkEnvironmentEnvironmentLink] | None = None
    EnvironmentName: StrictStr | None = None
    OptionSettings: list[SecurityHubAwsElasticBeanstalkEnvironmentOptionSetting] | None = None
    PlatformArn: StrictStr | None = None
    SolutionStackName: StrictStr | None = None
    Status: StrictStr | None = None
    Tier: SecurityHubAwsElasticBeanstalkEnvironmentTier | None = None
    VersionLabel: StrictStr | None = None
