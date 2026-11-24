from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GluePIIDetection(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    PiiType: StrictStr | None = None
    EntityTypesToDetect: list[StrictStr] | None = None
    OutputColumnName: StrictStr | None = None
    SampleFraction: StrictFloat | StrictInt | None = None
    ThresholdFraction: StrictFloat | StrictInt | None = None
    MaskValue: StrictStr | None = None
    RedactText: StrictStr | None = None
    RedactChar: StrictStr | None = None
    MatchPattern: StrictStr | None = None
    NumLeftCharsToExclude: StrictInt | None = None
    NumRightCharsToExclude: StrictInt | None = None
    DetectionParameters: StrictStr | None = None
    DetectionSensitivity: StrictStr | None = None
