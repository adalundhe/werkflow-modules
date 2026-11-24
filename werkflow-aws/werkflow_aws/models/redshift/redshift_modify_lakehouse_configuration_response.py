from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftModifyLakehouseConfigurationResponse(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    LakehouseIdcApplicationArn: StrictStr | None = None
    LakehouseRegistrationStatus: StrictStr | None = None
    CatalogArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
