from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchTextOptions(BaseModel):
    DefaultValue: StrictStr | None = None
    SourceField: StrictStr | None = None
    ReturnEnabled: StrictBool | None = None
    SortEnabled: StrictBool | None = None
    HighlightEnabled: StrictBool | None = None
    AnalysisScheme: StrictStr | None = None
