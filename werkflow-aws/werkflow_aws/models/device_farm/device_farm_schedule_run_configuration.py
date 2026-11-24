from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .device_farm_customer_artifact_paths import DeviceFarmCustomerArtifactPaths
from .device_farm_device_proxy import DeviceFarmDeviceProxy
from .device_farm_environment_variable import DeviceFarmEnvironmentVariable
from .device_farm_location import DeviceFarmLocation
from .device_farm_radios import DeviceFarmRadios


class DeviceFarmScheduleRunConfiguration(BaseModel):
    extraDataPackageArn: StrictStr | None = None
    networkProfileArn: StrictStr | None = None
    locale: StrictStr | None = None
    location: DeviceFarmLocation | None = None
    vpceConfigurationArns: list[StrictStr] | None = None
    deviceProxy: DeviceFarmDeviceProxy | None = None
    customerArtifactPaths: DeviceFarmCustomerArtifactPaths | None = None
    radios: DeviceFarmRadios | None = None
    auxiliaryApps: list[StrictStr] | None = None
    billingMethod: Literal['METERED', 'UNMETERED'] | None = None
    environmentVariables: list[DeviceFarmEnvironmentVariable] | None = None
    executionRoleArn: StrictStr | None = None
    insightsTypes: list[Literal['TEST_REPORT', 'NONE']] | None = None
