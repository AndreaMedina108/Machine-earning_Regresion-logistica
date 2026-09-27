from scipy.optimize import minimize
from src.modelo import riesgo_logistico

def ajustar_modelo(x, y, theta_init=(0.0, 0.0), maxiter=None):
    """
    Minimiza el riesgo logístico utilizando scipy.optimize.minimize.
    Retorna el vector theta óptimo, el valor del riesgo mínimo y el estado de éxito.
    """
    options = {}
    if maxiter is not None:
        options['maxiter'] = maxiter
        
    res = minimize(
        fun=riesgo_logistico,
        x0=theta_init,
        args=(x, y),
        method='BFGS',  # Método de gradiente cuasi-Newton confiable
        options=options
    )
    
    return res.x, res.fun, res.success