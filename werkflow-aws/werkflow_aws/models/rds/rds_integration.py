from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rds_integration_error import RDSIntegrationError
from .rds_tag_model import RDSTagModel


class RDSIntegration(BaseModel):
    SourceArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    IntegrationName: StrictStr | None = None
    IntegrationArn: StrictStr | None = None
    KMSKeyId: StrictStr | None = None
    AdditionalEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Status: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
    DataFilter: StrictStr | None = None
    Description: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Errors: list[RDSIntegrationError] | None = None
