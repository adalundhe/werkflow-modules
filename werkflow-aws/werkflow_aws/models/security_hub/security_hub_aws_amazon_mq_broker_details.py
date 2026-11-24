from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_amazon_mq_broker_encryption_options_details import SecurityHubAwsAmazonMqBrokerEncryptionOptionsDetails
from .security_hub_aws_amazon_mq_broker_ldap_server_metadata_details import SecurityHubAwsAmazonMqBrokerLdapServerMetadataDetails
from .security_hub_aws_amazon_mq_broker_logs_details import SecurityHubAwsAmazonMqBrokerLogsDetails
from .security_hub_aws_amazon_mq_broker_maintenance_window_start_time_details import SecurityHubAwsAmazonMqBrokerMaintenanceWindowStartTimeDetails
from .security_hub_aws_amazon_mq_broker_users_details import SecurityHubAwsAmazonMqBrokerUsersDetails


class SecurityHubAwsAmazonMqBrokerDetails(BaseModel):
    AuthenticationStrategy: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    BrokerArn: StrictStr | None = None
    BrokerName: StrictStr | None = None
    DeploymentMode: StrictStr | None = None
    EncryptionOptions: SecurityHubAwsAmazonMqBrokerEncryptionOptionsDetails | None = None
    EngineType: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
    BrokerId: StrictStr | None = None
    LdapServerMetadata: SecurityHubAwsAmazonMqBrokerLdapServerMetadataDetails | None = None
    Logs: SecurityHubAwsAmazonMqBrokerLogsDetails | None = None
    MaintenanceWindowStartTime: SecurityHubAwsAmazonMqBrokerMaintenanceWindowStartTimeDetails | None = None
    PubliclyAccessible: StrictBool | None = None
    SecurityGroups: list[StrictStr] | None = None
    StorageType: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    Users: list[SecurityHubAwsAmazonMqBrokerUsersDetails] | None = None
