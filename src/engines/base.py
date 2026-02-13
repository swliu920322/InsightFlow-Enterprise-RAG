# src/engines/base.py
from abc import ABC, abstractmethod


class BaseRAGEngine(ABC):
    @abstractmethod
    async def stream_query(self, query: str, trace_id: str) -> dict:
        """
        Enforce auditability. Every query must carry a trace_id
        to ensure zero-trust compliance in financial auditing.
        """
        pass