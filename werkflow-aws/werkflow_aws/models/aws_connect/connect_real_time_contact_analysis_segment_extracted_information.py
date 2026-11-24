from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_extracted_information_value import ConnectRealTimeContactAnalysisExtractedInformationValue


class ConnectRealTimeContactAnalysisSegmentExtractedInformation(BaseModel):
    ExtractionDefinitionId: StrictStr | None = None
    ExtractionDefinitionName: StrictStr | None = None
    ExtractionDefinitionDisplayLabel: StrictStr | None = None
    ExtractedValues: list[ConnectRealTimeContactAnalysisExtractedInformationValue] | None = None
    FailureCode: StrictStr | None = None
