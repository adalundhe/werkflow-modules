from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchTextArrayOptions(BaseModel):
    DefaultValue: StrictStr | None = None
    SourceFields: StrictStr | None = None
    ReturnEnabled: StrictBool | None = None
    HighlightEnabled: StrictBool | None = None
    AnalysisScheme: StrictStr | None = None
