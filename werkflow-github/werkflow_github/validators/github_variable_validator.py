from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Union


class GithubVariable(BaseModel):
    name: StrictStr
    value: Union[StrictStr, StrictInt, StrictBool] 