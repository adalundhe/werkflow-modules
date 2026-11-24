from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_rds_db_cluster_associated_role import SecurityHubAwsRdsDbClusterAssociatedRole
from .security_hub_aws_rds_db_cluster_member import SecurityHubAwsRdsDbClusterMember
from .security_hub_aws_rds_db_cluster_option_group_membership import SecurityHubAwsRdsDbClusterOptionGroupMembership
from .security_hub_aws_rds_db_domain_membership import SecurityHubAwsRdsDbDomainMembership
from .security_hub_aws_rds_db_instance_vpc_security_group import SecurityHubAwsRdsDbInstanceVpcSecurityGroup


class SecurityHubAwsRdsDbClusterDetails(BaseModel):
    AllocatedStorage: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DatabaseName: StrictStr | None = None
    Status: StrictStr | None = None
    Endpoint: StrictStr | None = None
    ReaderEndpoint: StrictStr | None = None
    CustomEndpoints: list[StrictStr] | None = None
    MultiAz: StrictBool | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ReadReplicaIdentifiers: list[StrictStr] | None = None
    VpcSecurityGroups: list[SecurityHubAwsRdsDbInstanceVpcSecurityGroup] | None = None
    HostedZoneId: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbClusterResourceId: StrictStr | None = None
    AssociatedRoles: list[SecurityHubAwsRdsDbClusterAssociatedRole] | None = None
    ClusterCreateTime: StrictStr | None = None
    EnabledCloudWatchLogsExports: list[StrictStr] | None = None
    EngineMode: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    HttpEndpointEnabled: StrictBool | None = None
    ActivityStreamStatus: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    CrossAccountClone: StrictBool | None = None
    DomainMemberships: list[SecurityHubAwsRdsDbDomainMembership] | None = None
    DbClusterParameterGroup: StrictStr | None = None
    DbSubnetGroup: StrictStr | None = None
    DbClusterOptionGroupMemberships: list[SecurityHubAwsRdsDbClusterOptionGroupMembership] | None = None
    DbClusterIdentifier: StrictStr | None = None
    DbClusterMembers: list[SecurityHubAwsRdsDbClusterMember] | None = None
    IamDatabaseAuthenticationEnabled: StrictBool | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
