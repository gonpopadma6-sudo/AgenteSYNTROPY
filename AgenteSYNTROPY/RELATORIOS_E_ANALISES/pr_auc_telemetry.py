import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc
import numpy as np

# Avaliação da Curva PR-AUC em Sistemas Maiêuticos
# Focado na mitigação de problemas da matriz de confusão convencional (ROC-AUC)

# Y Real:
# 1 = Momento em que o agente DEVERIA ter intervindo (Humano precisava de andaime)
# 0 = Momento de Estado de Fluxo, NÃO interceder.
y_true = np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0])

# Predição (Probabilidade de intervenção gerada pela IA)
y_scores = np.array([0.9, 0.1, 0.05, 0.2, 0.85, 0.15, 0.1, 0.4, 0.05, 0.01])

def plot_syntropy_pr_auc(y_ground, y_probs):
    """
    Calcula e plota a Precision-Recall Area Under Curve.
    Um alto Recall com Alta Precisão significa que a IA agiu sem
    sobrecarregar o estado de fluxo com falsos alarmes (Automação predatória).
    """
    precision, recall, _ = precision_recall_curve(y_ground, y_probs)
    pr_auc = auc(recall, precision)

    print(f"====== Telemetria de Avaliação SYNTROPY ======")
    print(f"Área sob a Curva PR (AUPRC): {pr_auc:.3f}")
    
    # Análise Descritiva:
    # Falso Positivo (Alarmes Injustificados e Hiper-Automação)
    # Falso Negativo (Omissão Epistêmica e Latência Crítica no Connection Before Correction)
    if pr_auc > 0.85:
        print("Status: EXCELENTE. Calibração perfeitamente alinhada em Fluxo e Intervenção.")
    else:
        print("Status: ALERTA. O limiar de disparo deve ser ajustado para evitar quebra do Flow State.")

    # Em ambientes visuais o plt pode mostrar o gráfico real:
    # plt.plot(recall, precision, marker='.')
    # plt.title('SYNTROPY - Curva Precision-Recall (Intervenção vs Flow)')
    # plt.xlabel('Recall (Correção Evitada de Omissão)')
    # plt.ylabel('Precision (Mitigação de Hiper-Automação)')
    # plt.show()

if __name__ == "__main__":
    plot_syntropy_pr_auc(y_true, y_scores)
