from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class FirehoseOrcSerDe(BaseModel):
    StripeSizeBytes: StrictInt | None = None
    BlockSizeBytes: StrictInt | None = None
    RowIndexStride: StrictInt | None = None
    EnablePadding: StrictBool | None = None
    PaddingTolerance: StrictFloat | StrictInt | None = None
    Compression: StrictStr | None = None
    BloomFilterColumns: list[StrictStr] | None = None
    BloomFilterFalsePositiveProbability: StrictFloat | StrictInt | None = None
    DictionaryKeyThreshold: StrictFloat | StrictInt | None = None
    FormatVersion: StrictStr | None = None
