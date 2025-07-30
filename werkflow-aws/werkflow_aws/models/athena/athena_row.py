from pydantic import BaseModel
from .athena_var_char_value import AthenaVarCharValue

class AthenaRow(BaseModel):
    Data: list[AthenaVarCharValue]