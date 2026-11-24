from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .glue_code_gen_configuration_node import GlueCodeGenConfigurationNode
from .glue_connections_list import GlueConnectionsList
from .glue_execution_property import GlueExecutionProperty
from .glue_job_command import GlueJobCommand
from .glue_notification_property import GlueNotificationProperty
from .glue_source_control_details import GlueSourceControlDetails


class GlueCreateJobRequest(BaseModel):
    Name: StrictStr
    Role: StrictStr
    Command: GlueJobCommand
    JobMode: Literal['SCRIPT', 'VISUAL', 'NOTEBOOK'] | None = None
    JobRunQueuingEnabled: StrictBool | None = None
    Description: StrictStr | None = None
    LogUri: StrictStr | None = None
    ExecutionProperty: GlueExecutionProperty | None = None
    DefaultArguments: dict[StrictStr, StrictStr] | None = None
    NonOverridableArguments: dict[StrictStr, StrictStr] | None = None
    Connections: GlueConnectionsList | None = None
    MaxRetries: StrictInt | None = None
    AllocatedCapacity: StrictInt | None = None
    Timeout: StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    NotificationProperty: GlueNotificationProperty | None = None
    GlueVersion: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    WorkerType: Literal['Standard', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'G.025X', 'Z.2X', 'G.12X', 'G.16X', 'R.1X', 'R.2X', 'R.4X', 'R.8X'] | None = None
    CodeGenConfigurationNodes: dict[StrictStr, GlueCodeGenConfigurationNode] | None = None
    ExecutionClass: Literal['FLEX', 'STANDARD'] | None = None
    SourceControlDetails: GlueSourceControlDetails | None = None
    MaintenanceWindow: StrictStr | None = None
