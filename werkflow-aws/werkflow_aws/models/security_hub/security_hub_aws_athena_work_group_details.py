from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_athena_work_group_configuration_details import SecurityHubAwsAthenaWorkGroupConfigurationDetails


class SecurityHubAwsAthenaWorkGroupDetails(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    State: StrictStr | None = None
    Configuration: SecurityHubAwsAthenaWorkGroupConfigurationDetails | None = None
