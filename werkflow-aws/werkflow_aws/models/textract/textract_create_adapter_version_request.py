from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_adapter_version_dataset_config import TextractAdapterVersionDatasetConfig
from .textract_output_config import TextractOutputConfig


class TextractCreateAdapterVersionRequest(BaseModel):
    AdapterId: StrictStr
    DatasetConfig: TextractAdapterVersionDatasetConfig
    OutputConfig: TextractOutputConfig
    ClientRequestToken: StrictStr | None = None
    KMSKeyId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
