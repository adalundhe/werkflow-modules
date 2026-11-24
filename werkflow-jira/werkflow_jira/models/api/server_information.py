from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .health_check_result import HealthCheckResult


class ServerInformation(BaseModel):
    baseUrl: StrictStr | None = None
    buildDate: StrictStr | None = None
    buildNumber: StrictInt | None = None
    deploymentType: StrictStr | None = None
    displayUrl: StrictStr | None = None
    displayUrlConfluence: StrictStr | None = None
    displayUrlServicedeskHelpCenter: StrictStr | None = None
    healthChecks: list[HealthCheckResult] | None = None
    scmInfo: StrictStr | None = None
    serverTime: StrictStr | None = None
    serverTimeZone: StrictStr | None = None
    serverTitle: StrictStr | None = None
    version: StrictStr | None = None
    versionNumbers: list[StrictInt] | None = None
