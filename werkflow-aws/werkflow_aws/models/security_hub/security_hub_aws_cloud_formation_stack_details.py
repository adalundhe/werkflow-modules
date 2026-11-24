from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_cloud_formation_stack_drift_information_details import SecurityHubAwsCloudFormationStackDriftInformationDetails
from .security_hub_aws_cloud_formation_stack_outputs_details import SecurityHubAwsCloudFormationStackOutputsDetails


class SecurityHubAwsCloudFormationStackDetails(BaseModel):
    Capabilities: list[StrictStr] | None = None
    CreationTime: StrictStr | None = None
    Description: StrictStr | None = None
    DisableRollback: StrictBool | None = None
    DriftInformation: SecurityHubAwsCloudFormationStackDriftInformationDetails | None = None
    EnableTerminationProtection: StrictBool | None = None
    LastUpdatedTime: StrictStr | None = None
    NotificationArns: list[StrictStr] | None = None
    Outputs: list[SecurityHubAwsCloudFormationStackOutputsDetails] | None = None
    RoleArn: StrictStr | None = None
    StackId: StrictStr | None = None
    StackName: StrictStr | None = None
    StackStatus: StrictStr | None = None
    StackStatusReason: StrictStr | None = None
    TimeoutInMinutes: StrictInt | None = None
