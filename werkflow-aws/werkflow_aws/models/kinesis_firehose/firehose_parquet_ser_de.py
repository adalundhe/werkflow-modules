from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FirehoseParquetSerDe(BaseModel):
    BlockSizeBytes: StrictInt | None = None
    PageSizeBytes: StrictInt | None = None
    Compression: StrictStr | None = None
    EnableDictionaryCompression: StrictBool | None = None
    MaxPaddingBytes: StrictInt | None = None
    WriterVersion: StrictStr | None = None
