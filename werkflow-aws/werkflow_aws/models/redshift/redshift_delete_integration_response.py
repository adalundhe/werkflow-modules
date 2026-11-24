from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_integration_error import RedshiftIntegrationError
from .redshift_tag import RedshiftTag


class RedshiftDeleteIntegrationResponse(BaseModel):
    IntegrationArn: StrictStr | None = None
    IntegrationName: StrictStr | None = None
    SourceArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    Status: StrictStr | None = None
    Errors: list[RedshiftIntegrationError] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    KMSKeyId: StrictStr | None = None
    AdditionalEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Tags: list[RedshiftTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
