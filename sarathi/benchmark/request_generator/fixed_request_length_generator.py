from typing import Tuple

from sarathi.benchmark.request_generator.base_request_length_generator import (
    BaseRequestLengthGenerator, )


class FixedRequestLengthGenerator(BaseRequestLengthGenerator):

    def get_next_num_tokens(self) -> Tuple[float, float]:
        return self._config.fixed_request_length_generator_prefill_tokens, \
            self._config.fixed_request_length_generator_decode_tokens
