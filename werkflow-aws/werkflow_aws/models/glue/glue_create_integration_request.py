from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_integration_config import GlueIntegrationConfig
from .glue_tag import GlueTag


class GlueCreateIntegrationRequest(BaseModel):
    IntegrationName: StrictStr
    SourceArn: StrictStr
    TargetArn: StrictStr
    Description: StrictStr | None = None
    DataFilter: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    AdditionalEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Tags: list[GlueTag] | None = None
    IntegrationConfig: GlueIntegrationConfig | None = None
