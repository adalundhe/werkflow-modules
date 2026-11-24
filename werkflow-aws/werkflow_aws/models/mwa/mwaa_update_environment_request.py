from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .mwaa_identity_center_configuration import MWAAIdentityCenterConfiguration
from .mwaa_logging_configuration_input import MWAALoggingConfigurationInput
from .mwaa_update_network_configuration_input import MWAAUpdateNetworkConfigurationInput
from .mwaa_update_teams_input import MWAAUpdateTeamsInput


class MWAAUpdateEnvironmentRequest(BaseModel):
    Name: StrictStr
    ExecutionRoleArn: StrictStr | None = None
    AirflowConfigurationOptions: dict[StrictStr, StrictStr] | None = None
    AirflowVersion: StrictStr | None = None
    DagS3Path: StrictStr | None = None
    EnvironmentClass: StrictStr | None = None
    LoggingConfiguration: MWAALoggingConfigurationInput | None = None
    MaxWorkers: StrictInt | None = None
    MinWorkers: StrictInt | None = None
    MaxWebservers: StrictInt | None = None
    MinWebservers: StrictInt | None = None
    WorkerReplacementStrategy: Literal['FORCED', 'GRACEFUL'] | None = None
    NetworkConfiguration: MWAAUpdateNetworkConfigurationInput | None = None
    PluginsS3Path: StrictStr | None = None
    PluginsS3ObjectVersion: StrictStr | None = None
    RequirementsS3Path: StrictStr | None = None
    RequirementsS3ObjectVersion: StrictStr | None = None
    Schedulers: StrictInt | None = None
    SourceBucketArn: StrictStr | None = None
    StartupScriptS3Path: StrictStr | None = None
    StartupScriptS3ObjectVersion: StrictStr | None = None
    WebserverAccessMode: Literal['PRIVATE_ONLY', 'PUBLIC_ONLY', 'PUBLIC_AND_PRIVATE'] | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    IdentityCenterConfiguration: MWAAIdentityCenterConfiguration | None = None
    Teams: MWAAUpdateTeamsInput | None = None
