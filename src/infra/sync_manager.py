
import json
import os
import datetime
from typing import Dict, Any

class SyncManager:
    """
    Gerencia a sincronização entre o conhecimento interno do agente
    e o estado real do ambiente Antigravity.
    """
    
    MANIFEST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../SYSTEM_CORE/capabilities_manifest.json'))

    def load_manifest(self) -> Dict[str, Any]:
        """Carrega o manifesto de capacidades."""
        if not os.path.exists(self.MANIFEST_PATH):
            return {}
        with open(self.MANIFEST_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)

    def update_sync_date(self):
        """Atualiza a data da última sincronização no manifesto."""
        data = self.load_manifest()
        data["last_sync"] = datetime.date.today().isoformat()
        
        with open(self.MANIFEST_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return data

    def get_current_capabilities(self) -> str:
        """Retorna uma string resumida das capacidades para injeção de contexto."""
        data = self.load_manifest()
        env = data.get("environment", {})
        models = ", ".join(env.get("available_models", []))
        return f"Antigravity v{env.get('antigravity_version')}. Modelos: {models}. Ultima Atualização: {data.get('update_notes')}"

if __name__ == "__main__":
    manager = SyncManager()
    print(manager.get_current_capabilities())
