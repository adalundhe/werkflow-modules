from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_f_sx_lustre_config import SageMakerFSxLustreConfig


class SageMakerClusterSharedEnvironmentConfigDetails(BaseModel):
    CurrentFSxLustreConfig: SageMakerFSxLustreConfig | None = None
    DesiredFSxLustreConfig: SageMakerFSxLustreConfig | None = None
    CurrentFSxLustreDeletionPolicy: StrictStr | None = None
    DesiredFSxLustreDeletionPolicy: StrictStr | None = None
