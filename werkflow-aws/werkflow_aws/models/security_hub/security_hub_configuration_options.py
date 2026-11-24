from __future__ import annotations
from pydantic import BaseModel
from .security_hub_boolean_configuration_options import SecurityHubBooleanConfigurationOptions
from .security_hub_double_configuration_options import SecurityHubDoubleConfigurationOptions
from .security_hub_enum_configuration_options import SecurityHubEnumConfigurationOptions
from .security_hub_enum_list_configuration_options import SecurityHubEnumListConfigurationOptions
from .security_hub_integer_configuration_options import SecurityHubIntegerConfigurationOptions
from .security_hub_integer_list_configuration_options import SecurityHubIntegerListConfigurationOptions
from .security_hub_string_configuration_options import SecurityHubStringConfigurationOptions
from .security_hub_string_list_configuration_options import SecurityHubStringListConfigurationOptions


class SecurityHubConfigurationOptions(BaseModel):
    Integer: SecurityHubIntegerConfigurationOptions | None = None
    IntegerList: SecurityHubIntegerListConfigurationOptions | None = None
    Double: SecurityHubDoubleConfigurationOptions | None = None
    String: SecurityHubStringConfigurationOptions | None = None
    StringList: SecurityHubStringListConfigurationOptions | None = None
    Boolean: SecurityHubBooleanConfigurationOptions | None = None
    Enum: SecurityHubEnumConfigurationOptions | None = None
    EnumList: SecurityHubEnumListConfigurationOptions | None = None
