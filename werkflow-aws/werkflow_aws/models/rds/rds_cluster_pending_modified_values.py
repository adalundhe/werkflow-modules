from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_certificate_details import RDSCertificateDetails
from .rds_pending_cloudwatch_logs_exports import RDSPendingCloudwatchLogsExports
from .rds_rds_custom_cluster_configuration import RDSRdsCustomClusterConfiguration


class RDSClusterPendingModifiedValues(BaseModel):
    PendingCloudwatchLogsExports: RDSPendingCloudwatchLogsExports | None = None
    DBClusterIdentifier: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    StorageType: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    RdsCustomClusterConfiguration: RDSRdsCustomClusterConfiguration | None = None
    Iops: StrictInt | None = None
    CertificateDetails: RDSCertificateDetails | None = None
    VPCNetworkingEnabled: StrictBool | None = None
    InternetAccessGatewayEnabled: StrictBool | None = None
