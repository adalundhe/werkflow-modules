from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .device_farm_counters import DeviceFarmCounters
from .device_farm_customer_artifact_paths import DeviceFarmCustomerArtifactPaths
from .device_farm_device_minutes import DeviceFarmDeviceMinutes
from .device_farm_device_proxy import DeviceFarmDeviceProxy
from .device_farm_device_selection_result import DeviceFarmDeviceSelectionResult
from .device_farm_environment_variable import DeviceFarmEnvironmentVariable
from .device_farm_location import DeviceFarmLocation
from .device_farm_network_profile import DeviceFarmNetworkProfile
from .device_farm_radios import DeviceFarmRadios
from .device_farm_run_insights import DeviceFarmRunInsights
from .device_farm_vpc_config import DeviceFarmVpcConfig


class DeviceFarmRun(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    platform: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    result: StrictStr | None = None
    started: datetime.datetime | StrictStr | None = None
    stopped: datetime.datetime | StrictStr | None = None
    counters: DeviceFarmCounters | None = None
    message: StrictStr | None = None
    totalJobs: StrictInt | None = None
    completedJobs: StrictInt | None = None
    billingMethod: StrictStr | None = None
    deviceMinutes: DeviceFarmDeviceMinutes | None = None
    networkProfile: DeviceFarmNetworkProfile | None = None
    deviceProxy: DeviceFarmDeviceProxy | None = None
    parsingResultUrl: StrictStr | None = None
    resultCode: StrictStr | None = None
    seed: StrictInt | None = None
    appUpload: StrictStr | None = None
    eventCount: StrictInt | None = None
    jobTimeoutMinutes: StrictInt | None = None
    devicePoolArn: StrictStr | None = None
    locale: StrictStr | None = None
    radios: DeviceFarmRadios | None = None
    location: DeviceFarmLocation | None = None
    customerArtifactPaths: DeviceFarmCustomerArtifactPaths | None = None
    webUrl: StrictStr | None = None
    skipAppResign: StrictBool | None = None
    testSpecArn: StrictStr | None = None
    testPackageArn: StrictStr | None = None
    deviceSelectionResult: DeviceFarmDeviceSelectionResult | None = None
    vpcConfig: DeviceFarmVpcConfig | None = None
    executionRoleArn: StrictStr | None = None
    environmentVariables: list[DeviceFarmEnvironmentVariable] | None = None
    insightsTypes: list[StrictStr] | None = None
    insights: DeviceFarmRunInsights | None = None
