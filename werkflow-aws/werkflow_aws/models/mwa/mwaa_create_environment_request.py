from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .mwaa_identity_center_configuration import MWAAIdentityCenterConfiguration
from .mwaa_logging_configuration_input import MWAALoggingConfigurationInput
from .mwaa_network_configuration import MWAANetworkConfiguration
from .mwaa_team_config import MWAATeamConfig


class MWAACreateEnvironmentRequest(BaseModel):
    Name: StrictStr
    ExecutionRoleArn: StrictStr
    SourceBucketArn: StrictStr
    DagS3Path: StrictStr
    NetworkConfiguration: MWAANetworkConfiguration
    PluginsS3Path: StrictStr | None = None
    PluginsS3ObjectVersion: StrictStr | None = None
    RequirementsS3Path: StrictStr | None = None
    RequirementsS3ObjectVersion: StrictStr | None = None
    StartupScriptS3Path: StrictStr | None = None
    StartupScriptS3ObjectVersion: StrictStr | None = None
    AirflowConfigurationOptions: dict[StrictStr, StrictStr] | None = None
    EnvironmentClass: StrictStr | None = None
    MaxWorkers: StrictInt | None = None
    KmsKey: StrictStr | None = None
    AirflowVersion: StrictStr | None = None
    LoggingConfiguration: MWAALoggingConfigurationInput | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    WebserverAccessMode: Literal['PRIVATE_ONLY', 'PUBLIC_ONLY', 'PUBLIC_AND_PRIVATE'] | None = None
    MinWorkers: StrictInt | None = None
    Schedulers: StrictInt | None = None
    EndpointManagement: Literal['CUSTOMER', 'SERVICE'] | None = None
    MinWebservers: StrictInt | None = None
    MaxWebservers: StrictInt | None = None
    IdentityCenterConfiguration: MWAAIdentityCenterConfiguration | None = None
    Teams: dict[StrictStr, MWAATeamConfig] | None = None
