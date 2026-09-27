# Exploración Computacional de la Regresión Logística

## Objetivo
Este proyecto implementa y evalúa computacionalmente un modelo de regresión logística desde cero, estudiando propiedades como la superficie de la función de riesgo empírico, el comportamiento frente a datos separables y no separables, la recuperación de parámetros poblacionales y la estabilidad numérica de la verosimilitud. Todo se ha implementado de forma modular sin usar `scikit-learn` con el fin de ver qué hace `scikit-learn` realmente, ya que en teoría `scikit-learn` tiene todo esto ya implementado.

## Integrantes
- Andrea Medina y Tatiana Casallas

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
Para reproducir el trabajo (asumiendo ya tenga python instalado y jupyter y git dentro de Visual Studio Code):
1. Abre la carpeta raíz del proyecto en Visual Studio Code.
2. Abre el archivo `notebooks/experimentos.ipynb`.
3. Asegúrate de seleccionar el entorno de Python correcto (kernel) en la esquina superior derecha.
4. Haz clic en "Run All" (o "Restart & Run All") para ejecutar todos los experimentos desde cero.
Las gráficas se generarán y guardarán físicamente de forma automática en la carpeta resultados/.
