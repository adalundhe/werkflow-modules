from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_certificate_details import DocumentDBCertificateDetails
from .document_dbdb_instance_status_info import DocumentDBDBInstanceStatusInfo
from .document_dbdb_subnet_group import DocumentDBDBSubnetGroup
from .document_db_endpoint import DocumentDBEndpoint
from .document_db_pending_modified_values import DocumentDBPendingModifiedValues
from .document_db_vpc_security_group_membership import DocumentDBVpcSecurityGroupMembership


class DocumentDBDBInstance(BaseModel):
    DBInstanceIdentifier: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Engine: StrictStr | None = None
    DBInstanceStatus: StrictStr | None = None
    Endpoint: DocumentDBEndpoint | None = None
    InstanceCreateTime: datetime.datetime | StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    VpcSecurityGroups: list[DocumentDBVpcSecurityGroupMembership] | None = None
    AvailabilityZone: StrictStr | None = None
    DBSubnetGroup: DocumentDBDBSubnetGroup | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    PendingModifiedValues: DocumentDBPendingModifiedValues | None = None
    LatestRestorableTime: datetime.datetime | StrictStr | None = None
    EngineVersion: StrictStr | None = None
    AutoMinorVersionUpgrade: StrictBool | None = None
    PubliclyAccessible: StrictBool | None = None
    StatusInfos: list[DocumentDBDBInstanceStatusInfo] | None = None
    DBClusterIdentifier: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    CACertificateIdentifier: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    PromotionTier: StrictInt | None = None
    DBInstanceArn: StrictStr | None = None
    EnabledCloudwatchLogsExports: list[StrictStr] | None = None
    CertificateDetails: DocumentDBCertificateDetails | None = None
    PerformanceInsightsEnabled: StrictBool | None = None
    PerformanceInsightsKMSKeyId: StrictStr | None = None
