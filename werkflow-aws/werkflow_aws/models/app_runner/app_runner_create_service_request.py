from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_encryption_configuration import AppRunnerEncryptionConfiguration
from .app_runner_health_check_configuration import AppRunnerHealthCheckConfiguration
from .app_runner_instance_configuration import AppRunnerInstanceConfiguration
from .app_runner_network_configuration import AppRunnerNetworkConfiguration
from .app_runner_service_observability_configuration import AppRunnerServiceObservabilityConfiguration
from .app_runner_source_configuration import AppRunnerSourceConfiguration
from .app_runner_tag import AppRunnerTag


class AppRunnerCreateServiceRequest(BaseModel):
    ServiceName: StrictStr
    SourceConfiguration: AppRunnerSourceConfiguration
    InstanceConfiguration: AppRunnerInstanceConfiguration | None = None
    Tags: list[AppRunnerTag] | None = None
    EncryptionConfiguration: AppRunnerEncryptionConfiguration | None = None
    HealthCheckConfiguration: AppRunnerHealthCheckConfiguration | None = None
    AutoScalingConfigurationArn: StrictStr | None = None
    NetworkConfiguration: AppRunnerNetworkConfiguration | None = None
    ObservabilityConfiguration: AppRunnerServiceObservabilityConfiguration | None = None
