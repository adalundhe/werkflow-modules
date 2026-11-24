from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .device_farm_schedule_run_configuration import DeviceFarmScheduleRunConfiguration
from .device_farm_schedule_run_test import DeviceFarmScheduleRunTest


class DeviceFarmGetDevicePoolCompatibilityRequest(BaseModel):
    devicePoolArn: StrictStr
    appArn: StrictStr | None = None
    testType: Literal['BUILTIN_FUZZ', 'APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_PYTHON', 'APPIUM_NODE', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_NODE', 'APPIUM_WEB_RUBY', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI'] | None = None
    test: DeviceFarmScheduleRunTest | None = None
    configuration: DeviceFarmScheduleRunConfiguration | None = None
    projectArn: StrictStr | None = None
