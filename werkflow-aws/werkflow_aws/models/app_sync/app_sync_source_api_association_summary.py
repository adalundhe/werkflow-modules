from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncSourceApiAssociationSummary(BaseModel):
    associationId: StrictStr | None = None
    associationArn: StrictStr | None = None
    sourceApiId: StrictStr | None = None
    sourceApiArn: StrictStr | None = None
    mergedApiId: StrictStr | None = None
    mergedApiArn: StrictStr | None = None
    description: StrictStr | None = None
