from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_input_data_config import TranslateInputDataConfig
from .translate_output_data_config import TranslateOutputDataConfig
from .translate_translation_settings import TranslateTranslationSettings


class TranslateStartTextTranslationJobRequest(BaseModel):
    InputDataConfig: TranslateInputDataConfig
    OutputDataConfig: TranslateOutputDataConfig
    DataAccessRoleArn: StrictStr
    SourceLanguageCode: StrictStr
    TargetLanguageCodes: list[StrictStr]
    ClientToken: StrictStr
    JobName: StrictStr | None = None
    TerminologyNames: list[StrictStr] | None = None
    ParallelDataNames: list[StrictStr] | None = None
    Settings: TranslateTranslationSettings | None = None
