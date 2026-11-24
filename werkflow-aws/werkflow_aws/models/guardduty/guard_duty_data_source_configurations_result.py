from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_cloud_trail_configuration_result import GuardDutyCloudTrailConfigurationResult
from .guard_duty_dns_logs_configuration_result import GuardDutyDNSLogsConfigurationResult
from .guard_duty_flow_logs_configuration_result import GuardDutyFlowLogsConfigurationResult
from .guard_duty_kubernetes_configuration_result import GuardDutyKubernetesConfigurationResult
from .guard_duty_malware_protection_configuration_result import GuardDutyMalwareProtectionConfigurationResult
from .guard_duty_s3_logs_configuration_result import GuardDutyS3LogsConfigurationResult


class GuardDutyDataSourceConfigurationsResult(BaseModel):
    CloudTrail: GuardDutyCloudTrailConfigurationResult | None = None
    DNSLogs: GuardDutyDNSLogsConfigurationResult | None = None
    FlowLogs: GuardDutyFlowLogsConfigurationResult | None = None
    S3Logs: GuardDutyS3LogsConfigurationResult | None = None
    Kubernetes: GuardDutyKubernetesConfigurationResult | None = None
    MalwareProtection: GuardDutyMalwareProtectionConfigurationResult | None = None
