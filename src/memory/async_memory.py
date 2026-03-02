
"""
Módulo de Gestão de Memória Assíncrona (Eixo III).
Execute indexação vetorial e compactação semântica em Threads de fundo
para não bloquear o loop principal do Agente (L0).
"""

import threading
import queue
import time
from typing import Dict, Any

class MemoryManager:
    def __init__(self):
        self.memory_queue = queue.Queue()
        self.is_running = True
        self.worker_thread = threading.Thread(target=self._background_worker, daemon=True)
        self.worker_thread.start()
        
        # Simulação de Vector DB
        self.vector_index = []

    def _background_worker(self):
        """Worker thread que consome a fila de memórias para persistência."""
        print("[MEMORY] Background Worker Started.")
        while self.is_running:
            try:
                # Bloqueia até ter item, timeout para checar is_running
                memory_item = self.memory_queue.get(timeout=1.0)
                self._process_memory_item(memory_item)
                self.memory_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"[MEMORY] Error in worker: {e}")

    def _process_memory_item(self, item: Dict[str, Any]):
        """
        Processa um item de memória (cálculo de embedding + indexação).
        Simula operação pesada (IO-bound / CPU-bound).
        """
        # 1. Compressão Semântica (Eixo III - Ação 3.2)
        # Se entropia for baixa (muito similar ao modelo atual), ignorar.
        entropy = self._calculate_entropy(item)
        if entropy < 0.2:
            return # Descartar ruído

        # 2. Indexação (Simulada)
        # time.sleep(0.05) # Simula latência de embedding
        self.vector_index.append(item)
        # print(f"[MEMORY] Persisted: {item['content']} (Entropy: {entropy:.2f})")

    def _calculate_entropy(self, item) -> float:
        """Mock: Calcula divergência semântica."""
        return 0.8 # Simula alta relevância por enquanto

    def enqueue_memory(self, content: str, metadata: Dict[str, Any]):
        """API pública: Enfileira memória para processamento assíncrono."""
        item = {
            "content": content,
            "metadata": metadata,
            "timestamp": time.time()
        }
        self.memory_queue.put(item)
    
    def shutdown(self):
        """Encerra graciosamente o worker."""
        self.is_running = False
        self.worker_thread.join()
        print("[MEMORY] Background Worker Stopped.")

# Singleton
memory_manager = MemoryManager()
