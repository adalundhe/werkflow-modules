from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .glue_auto_upgrade_metadata import GlueAutoUpgradeMetadata
from .glue_code_gen_configuration_node import GlueCodeGenConfigurationNode
from .glue_connections_list import GlueConnectionsList
from .glue_execution_property import GlueExecutionProperty
from .glue_job_command import GlueJobCommand
from .glue_notification_property import GlueNotificationProperty
from .glue_source_control_details import GlueSourceControlDetails


class GlueJob(BaseModel):
    Name: StrictStr | None = None
    JobMode: StrictStr | None = None
    JobRunQueuingEnabled: StrictBool | None = None
    Description: StrictStr | None = None
    LogUri: StrictStr | None = None
    Role: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    ExecutionProperty: GlueExecutionProperty | None = None
    Command: GlueJobCommand | None = None
    DefaultArguments: dict[StrictStr, StrictStr] | None = None
    NonOverridableArguments: dict[StrictStr, StrictStr] | None = None
    Connections: GlueConnectionsList | None = None
    MaxRetries: StrictInt | None = None
    AllocatedCapacity: StrictInt | None = None
    Timeout: StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    WorkerType: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    NotificationProperty: GlueNotificationProperty | None = None
    GlueVersion: StrictStr | None = None
    CodeGenConfigurationNodes: dict[StrictStr, GlueCodeGenConfigurationNode] | None = None
    ExecutionClass: StrictStr | None = None
    SourceControlDetails: GlueSourceControlDetails | None = None
    MaintenanceWindow: StrictStr | None = None
    ProfileName: StrictStr | None = None
    AutoUpgradeMetadata: GlueAutoUpgradeMetadata | None = None
