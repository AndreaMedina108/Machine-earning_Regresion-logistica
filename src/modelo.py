import numpy as np

def sigma(t):
    """Función sigmoide (logística)."""
    # Se recorta (clip) t para evitar overflow/underflow en np.exp
    t_clipped = np.clip(t, -500, 500)
    return 1.0 / (1.0 + np.exp(-t_clipped))

def p_theta(x, theta):
    """
    Calcula la probabilidad p_theta(x) para un modelo lineal 1D.
    theta = [theta_0, theta_1]
    """
    return sigma(theta[0] + theta[1] * x)

def riesgo_logistico(theta, x, y):
    """
    Calcula el riesgo empírico logístico (pérdida log-loss cruzada promedio).
    """
    p = p_theta(x, theta)
    
    # Recortar p para evitar evaluar log(0)
    epsilon = 1e-15
    p_clipped = np.clip(p, epsilon, 1.0 - epsilon)
    
    # log loss
    loss = y * np.log(p_clipped) + (1 - y) * np.log(1 - p_clipped)
    return -np.mean(loss)