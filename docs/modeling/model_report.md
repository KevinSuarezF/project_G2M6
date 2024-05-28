# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final desarrollado, basado en XGBoost Regressor, ha demostrado un rendimiento sobresaliente en las métricas de evaluación R^2 y EVS, con un valor de 0.909 para ambas. Este modelo supera significativamente al modelo base y otros modelos analizados, como Random Forest Regressor, Gradient Boosting Regressor y K Neighbors Regressor. Los hiperparámetros óptimos para el modelo XGBoost son {'n_estimators': 385, 'max_depth': 10, 'learning_rate': 0.0574}, obtenidos mediante un análisis exhaustivo de hiperparámetros.

## Descripción del Problema

El problema abordado consiste en predecir el precio de vehículos en el año 2018 a partir de un conjunto de características y variables relacionadas con los vehículos. Este problema es de relevancia en diversos sectores, incluyendo la industria automotriz, seguros y finanzas, donde la capacidad de predecir con precisión los precios de los vehículos puede ser crucial para la toma de decisiones estratégicas. El objetivo principal es desarrollar un modelo predictivo preciso que utilice las características específicas de los vehículos, como marca, clase, tipo de caja, nacionalidad, entre otras, para estimar el precio en el año 2018. La justificación de este modelo radica en su capacidad para proporcionar una herramienta útil para la valoración de vehículos y facilitar la toma de decisiones informadas en el mercado automotriz.

## Descripción del Modelo

El modelo final se basa en XGBoost (abreviatura de "extreme gradient boosting") Regressor, es un método de aprendizaje automático supervisado ampliamente utilizado en clasificación y regresión. Se basa en árboles de decisión y destaca por su eficacia en la predicción de datasets grandes y complejos. Utiliza diversas técnicas de optimización, como regularización, corte de ramas innecesarias y aprendizaje paralelo, para mejorar su rendimiento. Además, puede gestionar datos escasos y aprovechar eficientemente la memoria caché del sistema, incluso en el caso de datasets grandes que requieren computación fuera de núcleo. Estas características hacen de XGBoost una herramienta poderosa y versátil en el campo del aprendizaje automático. Se entrenó con los hiperparámetros óptimos encontrados: {'n_estimators': 385, 'max_depth': 10, 'learning_rate': 0.0574}. La metodología incluyó un análisis exhaustivo de hiperparámetros, validación cruzada y ajuste fino del modelo para maximizar el rendimiento predictivo.

## Evaluación del Modelo

El modelo final se evaluó utilizando las métricas de R^2 y EVS, que alcanzó un valor de 0.909 para ambas. Este resultado indica que el modelo es capaz de explicar aproximadamente el 91% de la variabilidad en la variable objetivo. El tiempo de entrenamiento del modelo fue de aproximadamente 38 minutos en total, lo que refleja la complejidad computacional del proceso de optimización de hiperparámetros.

## Conclusiones y Recomendaciones

El modelo final basado en XGBoost Regressor ha demostrado ser altamente efectivo en la predicción de la variable objetivo, superando a otros modelos analizados. Sus hiperparámetros óptimos permiten maximizar el rendimiento predictivo, aunque se debe tener en cuenta el tiempo de entrenamiento necesario para ajustar el modelo. Se recomienda aplicar el modelo en situaciones donde se requiera una alta precisión en la predicción de variables continuas y se disponga de recursos computacionales adecuados para el entrenamiento.

## Referencias

* Chen Tianqi y Guestrin Carlos. 2016. XGBoost: A scalable tree boosting system. En Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785–794.
* Friedman, J. H. (2001). Greedy Function Approximation: A Gradient Boosting Machine. Annals of Statistics, 29(5), 1189-1232.
* Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., ... & Liu, T. Y. (2017). LightGBM: A Highly Efficient Gradient Boosting Decision Tree. In Advances in Neural Information Processing Systems (pp. 3146-3154).
* Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Vanderplas, J. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(Oct), 2825-2830.
