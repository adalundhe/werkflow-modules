from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .redshift_integration_error import RedshiftIntegrationError


class RedshiftInboundIntegration(BaseModel):
    IntegrationArn: StrictStr | None = None
    SourceArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    Status: StrictStr | None = None
    Errors: list[RedshiftIntegrationError] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
