from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_describe_integrations_filter import RedshiftDescribeIntegrationsFilter


class RedshiftDescribeIntegrationsRequest(BaseModel):
    IntegrationArn: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    Filters: list[RedshiftDescribeIntegrationsFilter] | None = None
