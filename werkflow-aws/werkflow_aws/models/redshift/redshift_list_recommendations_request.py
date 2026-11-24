from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftListRecommendationsRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    NamespaceArn: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
