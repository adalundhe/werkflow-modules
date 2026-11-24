from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_custom_configuration import TextractCustomConfiguration
from .textract_encryption_configuration import TextractEncryptionConfiguration
from .textract_extraction_configuration import TextractExtractionConfiguration
from .textract_generative_configuration import TextractGenerativeConfiguration
from .textract_sensitive_data_configuration import TextractSensitiveDataConfiguration
from .textract_splitter_configuration import TextractSplitterConfiguration


class TextractCreateProjectRequest(BaseModel):
    ProjectName: StrictStr
    ExtractionConfiguration: TextractExtractionConfiguration
    ClientRequestToken: StrictStr | None = None
    ProjectDescription: StrictStr | None = None
    GenerativeConfiguration: TextractGenerativeConfiguration | None = None
    CustomConfiguration: TextractCustomConfiguration | None = None
    SplitterConfiguration: TextractSplitterConfiguration | None = None
    SensitiveDataConfiguration: TextractSensitiveDataConfiguration | None = None
    EncryptionConfiguration: TextractEncryptionConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
