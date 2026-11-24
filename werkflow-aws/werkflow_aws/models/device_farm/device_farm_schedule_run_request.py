from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_device_selection_configuration import DeviceFarmDeviceSelectionConfiguration
from .device_farm_execution_configuration import DeviceFarmExecutionConfiguration
from .device_farm_schedule_run_configuration import DeviceFarmScheduleRunConfiguration
from .device_farm_schedule_run_test import DeviceFarmScheduleRunTest


class DeviceFarmScheduleRunRequest(BaseModel):
    projectArn: StrictStr
    test: DeviceFarmScheduleRunTest
    appArn: StrictStr | None = None
    devicePoolArn: StrictStr | None = None
    deviceSelectionConfiguration: DeviceFarmDeviceSelectionConfiguration | None = None
    name: StrictStr | None = None
    configuration: DeviceFarmScheduleRunConfiguration | None = None
    executionConfiguration: DeviceFarmExecutionConfiguration | None = None
