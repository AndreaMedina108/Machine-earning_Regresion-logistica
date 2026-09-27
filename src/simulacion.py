import numpy as np
from src.modelo import p_theta

def generar_datos(n, theta_star, seed=2026):
    """
    Genera n datos usando el modelo generador logístico especificado.
    """
    rng = np.random.default_rng(seed)
    # X ~ U[-2, 2]
    x = rng.uniform(-2, 2, n)
    
    # Y ~ Bernoulli(p_theta*(X))
    p = p_theta(x, theta_star)
    y = rng.binomial(1, p)
    
    return x, y