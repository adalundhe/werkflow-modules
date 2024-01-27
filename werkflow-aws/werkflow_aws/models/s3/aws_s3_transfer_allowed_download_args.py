import datetime
from pydantic import StrictStr
from typing import Optional, Dict, Literal
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg,
    convert_key_to_boto3_arg_upper_matching,
    key_contains_patterns
)

class AWSs3TransferAllowedDownloadArgs(AWSBoto3Base):
    checksum_mode: Optional[
        Literal['ENABLED', 'DISABLED']
    ]=None
    version_id: Optional[StrictStr]=None
    sse_customer_algorithm: Optional[StrictStr]=None
    sse_customer_key: Optional[StrictStr]=None
    see_customer_key_md5: Optional[StrictStr]=None
    request_payer: Optional[Literal['requester']]=None
    expected_bucket_owner: Optional[StrictStr]=None

    def to_options(self):

        options = self._filtered_options_to_dict()

        uppercased_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                [
                    'md5', 
                    'crc32',
                    'crc32c',
                    'sha1',
                    'sha256',
                    'acp',
                    'sse',
                    'kms'
                ]
            ): value  for key, value in options.items() if key_contains_patterns(
                key,
                [
                    'sse_customer_algorithm',
                    'sse_customer_key',
                    'sse_customer_key_md5'
                ]
            )
        }

        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items() if key not in uppercased_options
        }

        parsed_options.update(uppercased_options)

        return parsed_options
