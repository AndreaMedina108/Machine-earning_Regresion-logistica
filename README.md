# Exploración Computacional de la Regresión Logística

## Objetivo
Este proyecto implementa y evalúa computacionalmente un modelo de regresión logística desde cero, estudiando propiedades como la superficie de la función de riesgo empírico, el comportamiento frente a datos separables y no separables, la recuperación de parámetros poblacionales, y la estabilidad numérica de la verosimilitud. Todo se ha implementado de forma modular sin usar `scikit-learn`.

## Integrantes
- [Tu Nombre / Tu Grupo]

## Estructura del repositorio
- `src/`: Contiene los módulos Python con la lógica base.
  - `modelo.py`: Funciones para la predicción logística y el cálculo del riesgo.
  - `optimizacion.py`: Lógica para el ajuste del modelo usando `scipy.optimize`.
  - `simulacion.py`: Funciones para la generación de datos simulados.
- `notebooks/`: Contiene `experimentos.ipynb` que importa los módulos de `src` y resuelve paso a paso los 5 ejercicios del taller.
- `resultados/`: Directorio donde el cuaderno guarda automáticamente las figuras generadas (`.png`).

## Instalación
Para instalar las dependencias requeridas en un entorno virtual local:
```bash
pip install -r requirements.txt
```

## Ejecución
Para reproducir el trabajo:
1. Navega a la raíz del proyecto.
2. Inicia Jupyter Notebook o JupyterLab (o usa Google Colab).
3. Abre el archivo `notebooks/experimentos.ipynb`.
4. Selecciona "Restart & Run All" en el kernel para ejecutar todos los experimentos desde cero y generar las gráficas en la carpeta `resultados/`.