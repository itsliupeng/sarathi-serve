import torch

from typing import List, Optional, Tuple
from sarathi.core.datatypes.sequence import SequenceMetadata
from sarathi.model_executor.attention.base_attention_wrapper import BaseAttentionWrapper


class NoOpAttentionWrapper(BaseAttentionWrapper):
    _inst = None

    def init(
        self,
        num_q_heads: int,
        num_kv_heads: int,
        head_dim: int,
        block_size: int,
        device: torch.device,
    ):
        self.device = device

    def get_cache_block(self, num_blocks: int,
                        **kwargs) -> Tuple[torch.Tensor, torch.Tensor]:
        pass

    def begin_forward(
        self,
        seq_metadata_list: List[SequenceMetadata],
    ) -> None:
        pass

    def end_forward(self):
        pass

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        kv_cache: Tuple[torch.Tensor, torch.Tensor],
        softmax_scale: float = 1.0,
        layer_id: Optional[int] = None,
    ) -> torch.Tensor:
        return torch.empty_like(query, device=self.device)
