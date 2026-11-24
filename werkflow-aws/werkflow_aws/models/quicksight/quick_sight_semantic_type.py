from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSemanticType(BaseModel):
    TypeName: StrictStr | None = None
    SubTypeName: StrictStr | None = None
    TypeParameters: dict[StrictStr, StrictStr] | None = None
    TruthyCellValue: StrictStr | None = None
    TruthyCellValueSynonyms: list[StrictStr] | None = None
    FalseyCellValue: StrictStr | None = None
    FalseyCellValueSynonyms: list[StrictStr] | None = None
