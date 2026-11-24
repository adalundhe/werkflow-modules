from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .translate_input_data_config import TranslateInputDataConfig
from .translate_job_details import TranslateJobDetails
from .translate_output_data_config import TranslateOutputDataConfig
from .translate_translation_settings import TranslateTranslationSettings


class TranslateTextTranslationJobProperties(BaseModel):
    JobId: StrictStr | None = None
    JobName: StrictStr | None = None
    JobStatus: StrictStr | None = None
    JobDetails: TranslateJobDetails | None = None
    SourceLanguageCode: StrictStr | None = None
    TargetLanguageCodes: list[StrictStr] | None = None
    TerminologyNames: list[StrictStr] | None = None
    ParallelDataNames: list[StrictStr] | None = None
    Message: StrictStr | None = None
    SubmittedTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    InputDataConfig: TranslateInputDataConfig | None = None
    OutputDataConfig: TranslateOutputDataConfig | None = None
    DataAccessRoleArn: StrictStr | None = None
    Settings: TranslateTranslationSettings | None = None
