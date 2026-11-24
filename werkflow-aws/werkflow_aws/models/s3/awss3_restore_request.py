from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_glacier_job_parameters import AWSS3GlacierJobParameters
from .awss3_output_location import AWSS3OutputLocation
from .awss3_select_parameters import AWSS3SelectParameters


class AWSS3RestoreRequest(BaseModel):
    Days: StrictInt | None = None
    GlacierJobParameters: AWSS3GlacierJobParameters | None = None
    Type: Literal['SELECT'] | None = None
    Tier: Literal['Standard', 'Bulk', 'Expedited'] | None = None
    Description: StrictStr | None = None
    SelectParameters: AWSS3SelectParameters | None = None
    OutputLocation: AWSS3OutputLocation | None = None
