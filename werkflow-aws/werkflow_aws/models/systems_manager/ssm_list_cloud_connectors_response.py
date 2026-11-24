from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_cloud_connector_summary import SSMCloudConnectorSummary


class SSMListCloudConnectorsResponse(BaseModel):
    CloudConnectors: list[SSMCloudConnectorSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
