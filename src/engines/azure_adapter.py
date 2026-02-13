from .base import BaseRAGEngine

class AzureNativeEngine(BaseRAGEngine):
    """
    Phase 2 (Roadmap - Spring 2026): Azure VNet 原生实现。
    完全解耦 Dify，使用 Azure AI Search + Azure OpenAI，满足政府级合规。
    """
    def __init__(self):
        # TODO: Initialize Azure AI Search & Azure OpenAI clients
        pass

    def query_with_citation(self, user_prompt: str, document_id: str) -> dict:
        raise NotImplementedError("Azure Native Engine is under construction (ETA: April 2026).")