import sys
import traceback

sys.path.append('src')

try:
    import orchestration.langgraph_maestro
    print("Sucesso!")
except Exception as e:
    traceback.print_exc()
