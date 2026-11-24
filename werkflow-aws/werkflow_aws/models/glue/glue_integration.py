from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_integration_config import GlueIntegrationConfig
from .glue_integration_error import GlueIntegrationError
from .glue_tag import GlueTag


class GlueIntegration(BaseModel):
    SourceArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    Description: StrictStr | None = None
    IntegrationName: StrictStr | None = None
    IntegrationArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    AdditionalEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Tags: list[GlueTag] | None = None
    Status: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    IntegrationConfig: GlueIntegrationConfig | None = None
    Errors: list[GlueIntegrationError] | None = None
    DataFilter: StrictStr | None = None
