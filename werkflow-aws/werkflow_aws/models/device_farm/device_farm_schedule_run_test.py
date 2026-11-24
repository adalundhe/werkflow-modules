from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DeviceFarmScheduleRunTest(BaseModel):
    type: Literal['BUILTIN_FUZZ', 'APPIUM_JAVA_JUNIT', 'APPIUM_JAVA_TESTNG', 'APPIUM_PYTHON', 'APPIUM_NODE', 'APPIUM_RUBY', 'APPIUM_WEB_JAVA_JUNIT', 'APPIUM_WEB_JAVA_TESTNG', 'APPIUM_WEB_PYTHON', 'APPIUM_WEB_NODE', 'APPIUM_WEB_RUBY', 'INSTRUMENTATION', 'XCTEST', 'XCTEST_UI']
    testPackageArn: StrictStr | None = None
    testSpecArn: StrictStr | None = None
    filter: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
