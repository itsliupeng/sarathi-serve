from vllm.utils.base_int_enum import BaseIntEnum


class RequestLengthGeneratorType(BaseIntEnum):
    UNIFORM = 1
    ZIPF = 2
    TRACE = 3
