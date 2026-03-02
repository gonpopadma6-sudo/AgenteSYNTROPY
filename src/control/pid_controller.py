
"""
Módulo de Controle PID Neural com Anti-Windup (Clamping e Back-Calculation).
Parte do Eixo I do Plano de Resolução Arquitetural do Agente SYNTROPY.
"""

class PIDController:
    def __init__(self, kp: float, ki: float, kd: float, saturation_limit: float = 1.0, kb: float = 0.5):
        """
        Inicializa o controlador PID.
        
        Args:
            kp (float): Ganho Proporcional.
            ki (float): Ganho Integral.
            kd (float): Ganho Derivativo.
            saturation_limit (float): Limite máximo de intervenção (U_s).
            kb (float): Ganho de Back-Calculation para Anti-Windup.
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.saturation_limit = saturation_limit
        self.kb = kb  # Ganho de rastreamento para back-calculation

        self.integral_sum = 0.0
        self.previous_error = 0.0
        self.previous_output = 0.0 # Para rastreamento de saturação

    def compute(self, setpoint: float, measured_value: float, dt: float) -> float:
        """
        Calcula a saída do controlador PID.

        Args:
            setpoint (float): Valor desejado (ex: carga cognitiva ideal).
            measured_value (float): Valor medido (ex: carga cognitiva atual).
            dt (float): Intervalo de tempo desde a última medição.

        Returns:
            float: Sinal de controle (u_t).
        """
        error = setpoint - measured_value

        # Termo Proporcional
        p_term = self.kp * error

        # Termo Derivativo
        d_term = 0.0
        if dt > 0:
            d_term = self.kd * (error - self.previous_error) / dt

        # Cálculo preliminar da saída (sem o novo termo integral completo ainda)
        # Usamos a soma integral anterior para estimar a saturação
        # Na verdade, para Back-Calculation, calculamos o termo integral ideal primeiro:
        
        # Integração padrão (sem proteção):
        # integral_term_candidate = self.integral_sum + (error * dt) 
        
        # Abordagem Back-Calculation:
        # u_v = Kp*e + Ki*Integral_anterior + Kd*de/dt
        # u = sat(u_v)
        # Novo Integral = Integral_anterior + Ki*e*dt + Kb*(u - u_v)*dt
        
        u_v = p_term + (self.ki * self.integral_sum) + d_term
        
        # Aplicar Saturação (Clamping na saída física)
        u_t = max(min(u_v, self.saturation_limit), -self.saturation_limit)
        
        # Back-Calculation para corrigir o termo integral
        # Diferença entre saída saturada e calculada
        desaturation_diff = u_t - u_v
        
        # Atualizar termo integral com correção
        self.integral_sum += (error * dt) + (self.kb * desaturation_diff * dt)
        
        # Clamping de segurança no próprio valor integral (opcional, mas recomendado)
        self.integral_sum = max(min(self.integral_sum, self.saturation_limit), -self.saturation_limit)

        self.previous_error = error
        self.previous_output = u_t
        return u_t

    def reset(self):
        """Reseta o estado do controlador."""
        self.integral_sum = 0.0
        self.previous_error = 0.0
        self.previous_output = 0.0

# Exemplo de uso (simulação):
# pid = PIDController(kp=1.0, ki=0.5, kd=0.1, saturation_limit=10.0)
# for i in range(100):
#     output = pid.compute(setpoint=0.0, measured_value=current_error, dt=0.1)
