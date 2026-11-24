from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .mq_configuration_id import MQConfigurationId
from .mq_encryption_options import MQEncryptionOptions
from .mq_ldap_server_metadata_input import MQLdapServerMetadataInput
from .mq_logs import MQLogs
from .mq_user import MQUser
from .mq_weekly_start_time import MQWeeklyStartTime


class MQCreateBrokerRequest(BaseModel):
    BrokerName: StrictStr
    DeploymentMode: Literal['SINGLE_INSTANCE', 'ACTIVE_STANDBY_MULTI_AZ', 'CLUSTER_MULTI_AZ']
    EngineType: Literal['ACTIVEMQ', 'RABBITMQ']
    HostInstanceType: StrictStr
    PubliclyAccessible: StrictBool
    AuthenticationStrategy: Literal['SIMPLE', 'LDAP', 'CONFIG_MANAGED'] | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    Configuration: MQConfigurationId | None = None
    CreatorRequestId: StrictStr | None = None
    EncryptionOptions: MQEncryptionOptions | None = None
    EngineVersion: StrictStr | None = None
    LdapServerMetadata: MQLdapServerMetadataInput | None = None
    Logs: MQLogs | None = None
    MaintenanceWindowStartTime: MQWeeklyStartTime | None = None
    SecurityGroups: list[StrictStr] | None = None
    StorageSize: StrictInt | None = None
    StorageType: Literal['EBS', 'EFS'] | None = None
    SubnetIds: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Users: list[MQUser] | None = None
    DataReplicationMode: Literal['NONE', 'CRDR'] | None = None
    DataReplicationPrimaryBrokerArn: StrictStr | None = None
