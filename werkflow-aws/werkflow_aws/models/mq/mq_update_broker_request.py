from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .mq_configuration_id import MQConfigurationId
from .mq_ldap_server_metadata_input import MQLdapServerMetadataInput
from .mq_logs import MQLogs
from .mq_weekly_start_time import MQWeeklyStartTime


class MQUpdateBrokerRequest(BaseModel):
    BrokerId: StrictStr
    AuthenticationStrategy: Literal['SIMPLE', 'LDAP', 'CONFIG_MANAGED'] | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    Configuration: MQConfigurationId | None = None
    EngineVersion: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
    LdapServerMetadata: MQLdapServerMetadataInput | None = None
    Logs: MQLogs | None = None
    MaintenanceWindowStartTime: MQWeeklyStartTime | None = None
    ResourceShareArns: list[StrictStr] | None = None
    SecurityGroups: list[StrictStr] | None = None
    StorageSize: StrictInt | None = None
    DataReplicationMode: Literal['NONE', 'CRDR'] | None = None
