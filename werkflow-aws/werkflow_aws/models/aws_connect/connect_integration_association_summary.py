from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectIntegrationAssociationSummary(BaseModel):
    IntegrationAssociationId: StrictStr | None = None
    IntegrationAssociationArn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    IntegrationType: StrictStr | None = None
    IntegrationArn: StrictStr | None = None
    SourceApplicationUrl: StrictStr | None = None
    SourceApplicationName: StrictStr | None = None
    SourceType: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
