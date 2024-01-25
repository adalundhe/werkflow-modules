from typing import List

def convert_key_to_boto3_arg(key: str):
    return ''.join([
        key_partial.capitalize() for key_partial in key.split('_')
    ])


def convert_key_to_boto3_arg_upper_matching(
    key: str,
    patterns: List[str]
):
    key_partials = key.split('_')

    partials: List[str] = []

    for partial in key_partials:
        if partial in patterns:
            partial = partial.upper()

        else:
            partial = partial.capitalize()

        partials.append(partial)

    return ''.join(partials)


def key_contains_patterns(
    key: str,
    patterns: List[str]
):
    return len([
        pattern for pattern in patterns if pattern in key
    ]) > 0