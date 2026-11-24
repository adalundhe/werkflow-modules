from typing import Any, Literal, Optional
from boto3.s3.transfer import TransferConfig
from pydantic import BaseModel, StrictBool, StrictInt


class AWSs3TransferConfigOptions(BaseModel):
    multipart_threshold: Optional[StrictInt] = None
    max_concurrency: Optional[StrictInt] = None
    multipart_chunksize: Optional[StrictInt] = None
    num_download_attempts: Optional[StrictInt] = None
    max_io_queue: Optional[StrictInt] = None
    io_chunksize: Optional[StrictInt] = None
    use_threads: Optional[StrictBool] = True
    max_bandwidth: Optional[StrictInt] = None
    preferred_transfer_client: Optional[Literal['auto', 'classic']] = 'auto'

    def to_transfer_config(self) -> TransferConfig:
        kwargs: dict[str, Any] = self.model_dump(exclude_none=True)
        return TransferConfig(**kwargs)
