from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_cloud_connector_filter import SSMCloudConnectorFilter


class SSMListCloudConnectorsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[SSMCloudConnectorFilter] | None = None
