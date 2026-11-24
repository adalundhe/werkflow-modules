from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_runner_auto_scaling_configuration_summary import AppRunnerAutoScalingConfigurationSummary
from .app_runner_encryption_configuration import AppRunnerEncryptionConfiguration
from .app_runner_health_check_configuration import AppRunnerHealthCheckConfiguration
from .app_runner_instance_configuration import AppRunnerInstanceConfiguration
from .app_runner_network_configuration import AppRunnerNetworkConfiguration
from .app_runner_service_observability_configuration import AppRunnerServiceObservabilityConfiguration
from .app_runner_source_configuration import AppRunnerSourceConfiguration


class AppRunnerService(BaseModel):
    ServiceName: StrictStr | None = None
    ServiceId: StrictStr | None = None
    ServiceArn: StrictStr | None = None
    ServiceUrl: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    DeletedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    SourceConfiguration: AppRunnerSourceConfiguration | None = None
    InstanceConfiguration: AppRunnerInstanceConfiguration | None = None
    EncryptionConfiguration: AppRunnerEncryptionConfiguration | None = None
    HealthCheckConfiguration: AppRunnerHealthCheckConfiguration | None = None
    AutoScalingConfigurationSummary: AppRunnerAutoScalingConfigurationSummary | None = None
    NetworkConfiguration: AppRunnerNetworkConfiguration | None = None
    ObservabilityConfiguration: AppRunnerServiceObservabilityConfiguration | None = None
