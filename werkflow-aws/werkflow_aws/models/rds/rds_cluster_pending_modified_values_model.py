from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_certificate_details_model import RDSCertificateDetailsModel
from .rds_pending_cloudwatch_logs_exports_model import RDSPendingCloudwatchLogsExportsModel
from .rds_custom_cluster_configuration import RdsCustomClusterConfiguration as _RdsCustomClusterConfigurationType


class RDSClusterPendingModifiedValuesModel(BaseModel):
    PendingCloudwatchLogsExports: RDSPendingCloudwatchLogsExportsModel | None = None
    DBClusterIdentifier: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    BackupRetentionPeriod: StrictInt | None = None
    StorageType: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    RdsCustomClusterConfiguration: _RdsCustomClusterConfigurationType | None = None
    Iops: StrictInt | None = None
    CertificateDetails: RDSCertificateDetailsModel | None = None
    VPCNetworkingEnabled: StrictBool | None = None
    InternetAccessGatewayEnabled: StrictBool | None = None
