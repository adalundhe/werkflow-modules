from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateIntegrationRequest(BaseModel):
    SourceArn: StrictStr
    TargetArn: StrictStr
    IntegrationName: StrictStr
    KMSKeyId: StrictStr | None = None
    AdditionalEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Tags: list[RDSTagModel] | None = None
    DataFilter: StrictStr | None = None
    Description: StrictStr | None = None
