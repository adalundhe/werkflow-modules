from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ai_adapter_model_package_entry import SageMakerAIAdapterModelPackageEntry
from .sage_maker_ai_adapter_s3_entry import SageMakerAIAdapterS3Entry


class SageMakerAIAdapterSource(BaseModel):
    ModelPackageArns: list[SageMakerAIAdapterModelPackageEntry] | None = None
    S3Uris: list[SageMakerAIAdapterS3Entry] | None = None
