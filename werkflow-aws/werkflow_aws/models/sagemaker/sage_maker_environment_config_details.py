from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_f_sx_lustre_config import SageMakerFSxLustreConfig


class SageMakerEnvironmentConfigDetails(BaseModel):
    FSxLustreConfig: SageMakerFSxLustreConfig | None = None
    S3OutputPath: StrictStr | None = None
