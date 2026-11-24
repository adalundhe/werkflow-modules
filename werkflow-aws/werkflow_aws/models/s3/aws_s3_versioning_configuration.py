from typing import Any, Literal, Optional
from werkflow_aws.models.base import AWSBoto3Base
from werkflow_aws.models.parsing import (
    convert_key_to_boto3_arg,
    convert_key_to_boto3_arg_upper_matching,
)


class AWSs3VersioningConfiguration(AWSBoto3Base):
    mfa_delete: Optional[Literal['Enabled', 'Disabled']] = None
    status: Optional[Literal['Enabled', 'Suspended']] = None

    def to_data(self) -> dict[str, Any]:
        options = self._filtered_options_to_dict()
        parsed: dict[str, Any] = {}
        for key, value in options.items():
            if key == 'mfa_delete':
                boto_key = convert_key_to_boto3_arg_upper_matching(key, ['mfa'])
            else:
                boto_key = convert_key_to_boto3_arg(key)
            parsed[boto_key] = value
        return parsed

    to_options = to_data
