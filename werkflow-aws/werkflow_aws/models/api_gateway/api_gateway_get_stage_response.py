from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_access_log_settings import APIGatewayAccessLogSettings
from .api_gateway_canary_settings import APIGatewayCanarySettings
from .api_gateway_method_setting import APIGatewayMethodSetting


class APIGatewayGetStageResponse(BaseModel):
    deploymentId: StrictStr | None = None
    clientCertificateId: StrictStr | None = None
    stageName: StrictStr | None = None
    description: StrictStr | None = None
    cacheClusterEnabled: StrictBool | None = None
    cacheClusterSize: StrictStr | None = None
    cacheClusterStatus: StrictStr | None = None
    methodSettings: dict[StrictStr, APIGatewayMethodSetting] | None = None
    variables: dict[StrictStr, StrictStr] | None = None
    documentationVersion: StrictStr | None = None
    accessLogSettings: APIGatewayAccessLogSettings | None = None
    canarySettings: APIGatewayCanarySettings | None = None
    tracingEnabled: StrictBool | None = None
    webAclArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
