from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_integration_config import GlueIntegrationConfig
from .glue_integration_error import GlueIntegrationError


class GlueInboundIntegration(BaseModel):
    SourceArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    IntegrationArn: StrictStr | None = None
    Status: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    IntegrationConfig: GlueIntegrationConfig | None = None
    Errors: list[GlueIntegrationError] | None = None
