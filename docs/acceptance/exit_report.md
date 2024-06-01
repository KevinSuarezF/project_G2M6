# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning destinado a predecir los precios de vehículos en Colombia para el año 2018. Se presentan los principales logros, desafíos y lecciones aprendidas durante el proceso, así como el impacto del modelo en el negocio y recomendaciones para futuros proyectos.

## Resultados del proyecto

### Resumen de los entregables y logros alcanzados

* Se desarrolló y evaluó un modelo baseline utilizando Support Vector Machine (SVM) para predecir precios de vehículos.
* Se exploraron y compararon otros modelos avanzados como RandomForestRegressor, GradientBoostingRegressor, XGBRegressor y KNeighborsRegressor.
* Se implementó el modelo XGBRegressor como el mejor modelo, logrando un coeficiente de determinación (R²) de 0.909 y un Explained Variance Score (EVS) de 0.909.
* Se desplegó el modelo final en una infraestructura basada en FastAPI, asegurando que estuviera listo para recibir y procesar solicitudes en tiempo real.


### Evaluación del modelo final y comparación con el modelo base

* El modelo baseline (SVM) obtuvo un R² de 0.4749 y un EVS de 0.5014.
* El modelo final (XGBRegressor) mostró una mejora significativa con un R² de 0.909 y un EVS de 0.909.
* Otros modelos como RandomForestRegressor, GradientBoostingRegressor y KNeighborsRegressor también superaron al modelo baseline, pero no alcanzaron el rendimiento del XGBRegressor.

### Descripción de los resultados y su relevancia para el negocio

* El modelo final permite realizar predicciones precisas de los precios de vehículos, facilitando la toma de decisiones informadas por parte del negocio.
* Una mejora en la precisión de las predicciones contribuye a una mejor planificación y estrategia de precios, optimizando los ingresos y la competitividad en el mercado.

## Lecciones aprendidas

### Identificación de los principales desafíos y obstáculos

* Manejo de un conjunto de datos con alta dimensionalidad y presencia de valores atípicos.
* Necesidad de preprocesar y escalar adecuadamente los datos para mejorar el rendimiento del modelo.
* Implementación y ajuste de hiperparámetros en modelos avanzados para maximizar su precisión.

### Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo

* La importancia de una exploración exhaustiva de los datos y un preprocesamiento riguroso para garantizar la calidad del modelo.
* La necesidad de comparar múltiples algoritmos y ajustar hiperparámetros para identificar el modelo más efectivo.
* La relevancia de una infraestructura de despliegue robusta y segura para asegurar la disponibilidad y eficiencia del modelo en producción.

## Impacto del proyecto

### Descripción del impacto del modelo en el negocio o en la industria

* Mejora significativa en la precisión de las predicciones de precios de vehículos, facilitando una mejor planificación y estrategia de ventas.
* Contribución a la competitividad del negocio mediante una estrategia de precios más informada y eficiente.
* Optimización de los ingresos y la satisfacción del cliente mediante precios más precisos y competitivos.

### Identificación de las áreas de mejora y oportunidades de desarrollo futuras

* Implementación de técnicas avanzadas de análisis y preprocesamiento de datos para mejorar aún más la calidad del conjunto de datos.
* Exploración de nuevos modelos y técnicas de machine learning para seguir mejorando la precisión y eficiencia del modelo.
* Desarrollo de una infraestructura más robusta y segura para el despliegue y mantenimiento del modelo en producción.

## Conclusiones

* Se logró desarrollar y desplegar un modelo de predicción de precios de vehículos con una alta precisión, superando significativamente al modelo baseline.
* Se establecieron procedimientos robustos para el preprocesamiento de datos, la selección y evaluación de modelos, y el despliegue en producción.
* El modelo XGBRegressor fue identificado como el más efectivo, logrando un R² de 0.909 y un EVS de 0.909.
* La importancia de una exploración exhaustiva y un preprocesamiento riguroso de los datos para el éxito del proyecto.
* La necesidad de comparar y ajustar múltiples modelos para identificar el más efectivo.
* La relevancia de una infraestructura de despliegue robusta y segura para asegurar la disponibilidad y eficiencia del modelo en producción.
* Continuar invirtiendo en herramientas y técnicas avanzadas de machine learning para seguir mejorando la precisión y eficiencia de los modelos.

## Agradecimientos

* Agradecimientos al equipo de data science (Kevin Suarez y Luis Angel Mazabuel) por su dedicación y esfuerzo en el desarrollo y despliegue del modelo.
* Agradecimientos a todo el equipo docente del Diplomado de Machine Learning & Data Science de la Universidad Nacional de Colombia que proporcionaron valiosas perspectivas y conocimientos sobre el desarrollo de aplicaciones con Machine Learning.
