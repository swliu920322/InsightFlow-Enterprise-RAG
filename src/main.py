from engine.dify_adapter import DifyEngineAdapter
from engine.azure_adapter import AzureNativeEngine

# 架构迭代开关：通过环境变量或配置切换底层引擎
CURRENT_PHASE = "PHASE_1_PROTOTYPE" # 未来改为 "PHASE_2_AZURE_NATIVE"

def get_rag_engine():
    """工厂模式：动态注入 RAG 引擎"""
    if CURRENT_PHASE == "PHASE_1_PROTOTYPE":
        return DifyEngineAdapter(api_key="your_dify_key")
    elif CURRENT_PHASE == "PHASE_2_AZURE_NATIVE":
        return AzureNativeEngine()
    else:
        raise ValueError("Unknown deployment phase.")

# API 路由
engine = get_rag_engine()
result = engine.query_with_citation("What are the risk factors?", "tsla-10k")
print(result)