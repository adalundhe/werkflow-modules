from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftModifyLakehouseConfigurationRequest(BaseModel):
    ClusterIdentifier: StrictStr
    LakehouseRegistration: Literal['Register', 'Deregister'] | None = None
    CatalogName: StrictStr | None = None
    LakehouseIdcRegistration: Literal['Associate', 'Disassociate'] | None = None
    LakehouseIdcApplicationArn: StrictStr | None = None
    DryRun: StrictBool | None = None
