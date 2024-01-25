import datetime
from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt,
)

from typing import Optional, Literal, Union
from werkflow_aws.models.base import AWSBoto3Options
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching
)



class AWSs3GetObjectOptions(AWSBoto3Options):
    if_match: Optional[StrictStr]
    if_modified_since: Optional[datetime.datetime]
    if_none_match: Optional[StrictStr]
    if_unmodified_since: Optional[datetime.datetime]
    range: Optional[StrictStr]
    response_cache_control: Optional[StrictStr]
    response_content_disposition: Optional[StrictStr]
    response_content_encoding: Optional[StrictStr]
    response_content_language: Optional[StrictStr]
    response_content_type: Optional[StrictStr]
    response_expires: Optional[datetime.datetime]
    version_id: Optional[StrictStr]
    sse_customer_algorithm: Optional[StrictStr]
    sse_customer_key: Optional[StrictStr]
    part_number: Optional[StrictInt]
    expected_bucket_owner: Optional[StrictStr]
    checksum_mode: Union[
        Optional[Literal['ENABLED']],
        Optional[Literal['DISABLED']]
    ]

    def to_options(self):

        options = self._filtered_options_to_dict()

        sse_options = {
            convert_key_to_boto3_arg_upper_matching(
                key,
                ['sse']
            ): value for key, value in options.items() if key.startswith('sse')
        }

        parsed_options = {
            convert_key_to_boto3_arg(
                key
            ): value for key, value in options.items()
        }

        parsed_options.update(sse_options)

        return parsed_options


