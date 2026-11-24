from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_target_platform import SageMakerTargetPlatform


class SageMakerOutputConfig(BaseModel):
    S3OutputLocation: StrictStr | None = None
    TargetDevice: StrictStr | None = None
    TargetPlatform: SageMakerTargetPlatform | None = None
    CompilerOptions: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
