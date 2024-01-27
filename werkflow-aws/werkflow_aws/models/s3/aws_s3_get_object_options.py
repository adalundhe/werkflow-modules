import datetime
from pydantic import (
    StrictStr,
    StrictInt
)

from typing import Optional, Literal
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg, 
    convert_key_to_boto3_arg_upper_matching
)



class AWSs3GetObjectOptions(AWSBoto3Base):
    if_match: Optional[StrictStr]=None
    if_modified_since: Optional[datetime.datetime]=None
    if_none_match: Optional[StrictStr]=None
    if_unmodified_since: Optional[datetime.datetime]=None
    range: Optional[StrictStr]=None
    response_cache_control: Optional[StrictStr]=None
    response_content_disposition: Optional[StrictStr]=None
    response_content_encoding: Optional[StrictStr]=None
    response_content_language: Optional[StrictStr]=None
    response_content_type: Optional[StrictStr]=None
    response_expires: Optional[datetime.datetime]=None
    version_id: Optional[StrictStr]=None
    sse_customer_algorithm: Optional[StrictStr]=None
    sse_customer_key: Optional[StrictStr]=None
    part_number: Optional[StrictInt]=None
    expected_bucket_owner: Optional[StrictStr]=None
    checksum_mode: Optional[
        Literal['ENABLED', 'DISABLED']
    ]=None

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


