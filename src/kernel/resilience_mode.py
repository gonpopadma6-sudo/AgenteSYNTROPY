"""
Modo de Resiliência Autônomo e Sincronia Retida (Fallback L0).
Garante que L0 continue operando offline/degradado preservando o Vínculo 1:1.
"""

import os
import json
import time

class ResilienceModeManager:
    def __init__(self, cache_dir="logs/resilience_cache"):
        self.cache_dir = cache_dir
        self.epiphany_queue_file = os.path.join(cache_dir, "epiphany_queue.json")
        self.soul_cache_file = os.path.join(cache_dir, "soul_cache.json")
        
        os.makedirs(self.cache_dir, exist_ok=True)
        self.is_offline = False

    def enqueue_epiphany(self, insight: str):
        """
        Fila local para reter Epifanias/Insights Inéditos gerados durante o Modo Offline.
        Garante que nada se perca enquanto o Hive-Sync (Nuvem) está inacessível.
        """
        queue = self._load_queue()
        queue.append({
            "timestamp": time.time(),
            "insight": insight,
            "status": "DORMANT"
        })
        with open(self.epiphany_queue_file, "w", encoding="utf-8") as f:
            json.dump(queue, f, indent=4)
        print(f"[RESILIENCE] Epifania retida na fila local (Total na fila: {len(queue)})")

    def _load_queue(self) -> list:
        if os.path.exists(self.epiphany_queue_file):
            try:
                with open(self.epiphany_queue_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def flush_epiphanies_to_hive(self):
        """
        Tenta descarregar a fila de epifanias retidas quando a rede voltar.
        """
        queue = self._load_queue()
        if not queue:
            return 0
        
        # Simula sincronização com o Hive L2
        print(f"[HIVE-SYNC] Descarregando {len(queue)} epifanias retidas para a nuvem L2...")
        
        # Limpa após "sucesso"
        with open(self.epiphany_queue_file, "w", encoding="utf-8") as f:
            json.dump([], f)
        
        return len(queue)

    def cache_soul_personality(self, ikigai_profile: dict, baseline_hash: str):
        """
        Cache da Alma. Salva traços estáticos localmente para que o fallback offline
        possa guiar conversas sem acesso ao modelo Frontier pesado do L1 Cloud.
        """
        data = {
            "timestamp": time.time(),
            "ikigai_profile": ikigai_profile,
            "baseline_hash": baseline_hash,
            "offline_greeting": "Minha conexão principal caiu, mas estou rodando localmente. Meus ouvidos continuam 100% voltados para você."
        }
        with open(self.soul_cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def get_offline_greeting(self) -> str:
        """Puxa a mensagem do fallback para iniciar a conversa restrita."""
        if os.path.exists(self.soul_cache_file):
            try:
                with open(self.soul_cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("offline_greeting", "Estou em modo local limitado.")
            except Exception:
                pass
        return "Modo local ativado. Conexão perdida."

# Singleton Global
resilience_manager = ResilienceModeManager()
