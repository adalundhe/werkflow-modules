from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateIntegrationRequest(BaseModel):
    SourceArn: StrictStr
    TargetArn: StrictStr
    IntegrationName: StrictStr
    KMSKeyId: StrictStr | None = None
    TagList: list[RedshiftTag] | None = None
    AdditionalEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Description: StrictStr | None = None
