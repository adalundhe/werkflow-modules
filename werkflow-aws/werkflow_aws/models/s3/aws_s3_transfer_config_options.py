from pydantic import (
    BaseModel,
    StrictInt, 
    StrictBool
)
from typing import Literal, Optional


class AWSs3TransferConfigOptions(BaseModel):
    multipart_threshold: Optional[StrictInt]=None
    max_concurrency: Optional[StrictInt]=None
    multipart_chunksize: Optional[StrictInt]=None
    num_download_attmpets: Optional[StrictInt]=None
    max_io_queue: Optional[StrictInt]=None
    io_chunksize: Optional[StrictInt]=None
    use_threads: Optional[StrictBool]=False
    max_bandwidth: Optional[StrictInt]=None
    preferred_trasfer_client: Optional[
        Literal[
            'auto',
            'classic'
        ]
    ]='auto'