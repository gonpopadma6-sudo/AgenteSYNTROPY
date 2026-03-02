
"""
Módulo de Roteamento de Hardware (Eixo II).
Projeto OpenClaw: Delegação dinâmica de inferência para NPU/GPU.
"""

from enum import Enum, auto
import platform
import time

class HardwareType(Enum):
    CPU = auto()
    GPU = auto()
    NPU = auto() # Neural Processing Unit (Apple Neural Engine, Intel VPU, etc)

class InferenceRouter:
    def __init__(self):
        self.available_hardware = self._detect_hardware()
        print(f"[OpenClaw] Hardware Detected: {self.available_hardware}")

    def _detect_hardware(self) -> dict:
        """
        Detecta aceleradores de hardware disponíveis no sistema.
        (Implementação mock para simulação).
        """
        hardware = {HardwareType.CPU: True, HardwareType.GPU: False, HardwareType.NPU: False}
        
        system = platform.system()
        processor = platform.processor()

        # Detecção Simples
        if "Apple" in processor or "arm" in processor: # Apple Silicon ou ARM
            hardware[HardwareType.NPU] = True
            hardware[HardwareType.GPU] = True
        
        # Em produção, usaríamos bibliotecas como 'torch.cuda.is_available()' 
        # ou 'intel_npu_acceleration_library'
        
        return hardware

    def route_task(self, task_type: str, input_data: any) -> HardwareType:
        """
        Decide onde executar uma tarefa baseada na sua natureza e hardware disponível.
        
        Prioridades:
        1. PII Stripping -> NPU (Eficiência/Segurança)
        2. Sentiment Analysis -> NPU (Baixa Latência)
        3. LLM Inference (Gen) -> GPU (VRAM) ou CPU (se pequeno/quantizado)
        """
        
        if task_type in ["pii_stripping", "sentiment_analysis"]:
            if self.available_hardware[HardwareType.NPU]:
                return HardwareType.NPU
            elif self.available_hardware[HardwareType.GPU]:
                return HardwareType.GPU
            else:
                return HardwareType.CPU
        
        elif task_type == "llm_generation_slm":
            if self.available_hardware[HardwareType.GPU]:
                return HardwareType.GPU
            if self.available_hardware[HardwareType.NPU]:
                 # SLMs modernos (ex: TinyLlama) rodam bem em NPUs
                return HardwareType.NPU
            return HardwareType.CPU
            
        return HardwareType.CPU

    def execute_inference(self, task_type: str, data: any):
        """Simula a execução da inferência no hardware roteado."""
        target_hw = self.route_task(task_type, data)
        start_time = time.time()
        
        # Simulação de latência baseada no hardware
        latency = 0.0
        if target_hw == HardwareType.NPU:
            latency = 0.05 # 50ms (Super rápido)
        elif target_hw == HardwareType.GPU:
            latency = 0.1 # 100ms
        else: # CPU
            latency = 0.4 # 400ms (Lento!)
            
        # time.sleep(latency) 
        
        print(f"[OpenClaw] Task '{task_type}' executed on {target_hw.name} in {latency*1000:.0f}ms")
        return {"status": "success", "hardware": target_hw.name, "latency": latency}

# Exemplo
# router = InferenceRouter()
# router.execute_inference("sentiment_analysis", "I feel happy")
