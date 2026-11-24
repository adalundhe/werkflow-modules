from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .mq_configuration_id import MQConfigurationId
from .mq_data_replication_metadata_output import MQDataReplicationMetadataOutput
from .mq_ldap_server_metadata_output import MQLdapServerMetadataOutput
from .mq_logs import MQLogs
from .mq_weekly_start_time import MQWeeklyStartTime


class MQUpdateBrokerResponse(BaseModel):
    AuthenticationStrategy: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    BrokerId: StrictStr | None = None
    Configuration: MQConfigurationId | None = None
    EngineVersion: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
    LdapServerMetadata: MQLdapServerMetadataOutput | None = None
    Logs: MQLogs | None = None
    MaintenanceWindowStartTime: MQWeeklyStartTime | None = None
    ResourceShareArns: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    DataReplicationMetadata: MQDataReplicationMetadataOutput | None = None
    DataReplicationMode: StrictStr | None = None
    PendingDataReplicationMetadata: MQDataReplicationMetadataOutput | None = None
    PendingDataReplicationMode: StrictStr | None = None
    StorageSize: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
