from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .mq_action_required import MQActionRequired
from .mq_broker_instance import MQBrokerInstance
from .mq_configurations import MQConfigurations
from .mq_data_replication_metadata_output import MQDataReplicationMetadataOutput
from .mq_encryption_options import MQEncryptionOptions
from .mq_ldap_server_metadata_output import MQLdapServerMetadataOutput
from .mq_logs_summary import MQLogsSummary
from .mq_user_summary import MQUserSummary
from .mq_weekly_start_time import MQWeeklyStartTime


class MQDescribeBrokerResponse(BaseModel):
    ActionsRequired: list[MQActionRequired] | None = None
    AuthenticationStrategy: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    BrokerArn: StrictStr | None = None
    BrokerId: StrictStr | None = None
    BrokerInstances: list[MQBrokerInstance] | None = None
    BrokerName: StrictStr | None = None
    BrokerState: StrictStr | None = None
    Configurations: MQConfigurations | None = None
    Created: datetime.datetime | StrictStr | None = None
    DeploymentMode: StrictStr | None = None
    EncryptionOptions: MQEncryptionOptions | None = None
    EngineType: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
    LdapServerMetadata: MQLdapServerMetadataOutput | None = None
    Logs: MQLogsSummary | None = None
    MaintenanceWindowStartTime: MQWeeklyStartTime | None = None
    PendingAuthenticationStrategy: StrictStr | None = None
    PendingEngineVersion: StrictStr | None = None
    PendingHostInstanceType: StrictStr | None = None
    PendingLdapServerMetadata: MQLdapServerMetadataOutput | None = None
    PendingSecurityGroups: list[StrictStr] | None = None
    PendingStorageSize: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
    SecurityGroups: list[StrictStr] | None = None
    StorageSize: StrictInt | None = None
    StorageType: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Users: list[MQUserSummary] | None = None
    DataReplicationMetadata: MQDataReplicationMetadataOutput | None = None
    DataReplicationMode: StrictStr | None = None
    PendingDataReplicationMetadata: MQDataReplicationMetadataOutput | None = None
    PendingDataReplicationMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
