from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_health_check_configuration import AppRunnerHealthCheckConfiguration
from .app_runner_instance_configuration import AppRunnerInstanceConfiguration
from .app_runner_network_configuration import AppRunnerNetworkConfiguration
from .app_runner_service_observability_configuration import AppRunnerServiceObservabilityConfiguration
from .app_runner_source_configuration import AppRunnerSourceConfiguration


class AppRunnerUpdateServiceRequest(BaseModel):
    ServiceArn: StrictStr
    SourceConfiguration: AppRunnerSourceConfiguration | None = None
    InstanceConfiguration: AppRunnerInstanceConfiguration | None = None
    AutoScalingConfigurationArn: StrictStr | None = None
    HealthCheckConfiguration: AppRunnerHealthCheckConfiguration | None = None
    NetworkConfiguration: AppRunnerNetworkConfiguration | None = None
    ObservabilityConfiguration: AppRunnerServiceObservabilityConfiguration | None = None
