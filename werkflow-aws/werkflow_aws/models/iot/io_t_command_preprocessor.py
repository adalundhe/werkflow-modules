from __future__ import annotations
from pydantic import BaseModel
from .io_t_aws_json_substitution_command_preprocessor_config import IoTAwsJsonSubstitutionCommandPreprocessorConfig


class IoTCommandPreprocessor(BaseModel):
    awsJsonSubstitution: IoTAwsJsonSubstitutionCommandPreprocessorConfig | None = None
