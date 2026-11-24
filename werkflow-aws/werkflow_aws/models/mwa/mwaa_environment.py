from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .mwaa_identity_center_configuration import MWAAIdentityCenterConfiguration
from .mwaa_last_update import MWAALastUpdate
from .mwaa_logging_configuration import MWAALoggingConfiguration
from .mwaa_network_configuration import MWAANetworkConfiguration
from .mwaa_team_config import MWAATeamConfig


class MWAAEnvironment(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    WebserverUrl: StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    ServiceRoleArn: StrictStr | None = None
    KmsKey: StrictStr | None = None
    AirflowVersion: StrictStr | None = None
    SourceBucketArn: StrictStr | None = None
    DagS3Path: StrictStr | None = None
    PluginsS3Path: StrictStr | None = None
    PluginsS3ObjectVersion: StrictStr | None = None
    RequirementsS3Path: StrictStr | None = None
    RequirementsS3ObjectVersion: StrictStr | None = None
    StartupScriptS3Path: StrictStr | None = None
    StartupScriptS3ObjectVersion: StrictStr | None = None
    AirflowConfigurationOptions: dict[StrictStr, StrictStr] | None = None
    EnvironmentClass: StrictStr | None = None
    MaxWorkers: StrictInt | None = None
    NetworkConfiguration: MWAANetworkConfiguration | None = None
    LoggingConfiguration: MWAALoggingConfiguration | None = None
    LastUpdate: MWAALastUpdate | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    WebserverAccessMode: StrictStr | None = None
    MinWorkers: StrictInt | None = None
    Schedulers: StrictInt | None = None
    WebserverVpcEndpointService: StrictStr | None = None
    DatabaseVpcEndpointService: StrictStr | None = None
    CeleryExecutorQueue: StrictStr | None = None
    EndpointManagement: StrictStr | None = None
    MinWebservers: StrictInt | None = None
    MaxWebservers: StrictInt | None = None
    IdentityCenterConfiguration: MWAAIdentityCenterConfiguration | None = None
    Teams: dict[StrictStr, MWAATeamConfig] | None = None
