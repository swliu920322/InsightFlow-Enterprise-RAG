# src/core/factory.py
from engines.base import BaseRAGEngine
from engines.dify_adapter import DifyAdapter
from engines.azure_native import AzureNativeEngine
from core.config import settings


class RAGEngineFactory:
    """
    Architectural Hub: Manages the lifecycle of RAG engines.
    Ensures seamless transition between Prototype (Dify) and Production (Azure).
    """

    @staticmethod
    def get_engine() -> BaseRAGEngine:
        if settings.DEPLOYMENT_PHASE == "PROTOTYPE":
            # Using Dify as the headless validation layer
            return DifyAdapter(api_key=settings.DIFY_API_KEY)

        # Phase 2: Switch to Azure Native Infrastructure
        return AzureNativeEngine(
            connection_string=settings.AZURE_SEARCH_CS,
            model_version="gpt-4-32k"
        )