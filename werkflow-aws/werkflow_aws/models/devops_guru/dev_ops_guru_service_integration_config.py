from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_kms_server_side_encryption_integration import DevOpsGuruKMSServerSideEncryptionIntegration
from .dev_ops_guru_logs_anomaly_detection_integration import DevOpsGuruLogsAnomalyDetectionIntegration
from .dev_ops_guru_ops_center_integration import DevOpsGuruOpsCenterIntegration


class DevOpsGuruServiceIntegrationConfig(BaseModel):
    OpsCenter: DevOpsGuruOpsCenterIntegration | None = None
    LogsAnomalyDetection: DevOpsGuruLogsAnomalyDetectionIntegration | None = None
    KMSServerSideEncryption: DevOpsGuruKMSServerSideEncryptionIntegration | None = None
