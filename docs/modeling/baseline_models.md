# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

Como modelo base elegimos un modelo altamente recomendado para regresiones el cual es robusto ante Outliers (Datos Atípicos) y ante espacios de alta dimensionalidad (nuestro dataset tiene 285 características y 9563 muestras).

Debido a que este modelo es suceptible ante diferencias entre escalas de los datos, nos aseguramos de que en el preprocesamiento todas las variables quedaran correctamente escaladas.

## Variables de entrada

Las variables de entrada o características (Features) del modelo son:

* 'Novedad_M' 'Novedad_N'
* 'Marca_ACURA' 'Marca_AG' 'Marca_AGRALE' 'Marca_AKT' 'Marca_ALEKO' 'Marca_ALFA ROMEO' 'Marca_AMC' 'Marca_AMPLE' 'Marca_APRILIA' 'Marca_ARCTIC CAT' 'Marca_AROCARPATI' 'Marca_ASIA' 'Marca_ATM' 'Marca_AUDI' 'Marca_AUPACO' 'Marca_AUTECO' 'Marca_AYCO' 'Marca_BAIC' 'Marca_BAW' 'Marca_BENELLI' 'Marca_BMW' 'Marca_BORGO' 'Marca_BRILLIANCE' 'Marca_BRP CAN AM' 'Marca_BUICK' 'Marca_BYD' 'Marca_CADILLAC' 'Marca_CAGIVA' 'Marca_CHANA' 'Marca_CHANGAN' 'Marca_CHANGFENG' 'Marca_CHANGHE' 'Marca_CHERY' 'Marca_CHEVROLET' 'Marca_CHRYSLER' 'Marca_CITROEN' 'Marca_CMC' 'Marca_DACIA' 'Marca_DADI' 'Marca_DAEWOO' 'Marca_DAF' 'Marca_DAIHATSU' 'Marca_DAYANG' 'Marca_DERBI' 'Marca_DFAC' 'Marca_DFSK/DFM/DFZL' 'Marca_DINA' 'Marca_DODGE' 'Marca_DONGBEN' 'Marca_DS' 'Marca_DUCATI' 'Marca_EAGLE CARGO' 'Marca_EUROPAMOTOS' 'Marca_EUROSTAR D`LONG' 'Marca_FAW AMI' 'Marca_FERRARI' 'Marca_FIAT' 'Marca_FIRENZE' 'Marca_FORD' 'Marca_FOTON' 'Marca_FREIGHTLINER' 'Marca_FUSO' 'Marca_GEELY' 'Marca_GLOW' 'Marca_GMC' 'Marca_GOLDEN DRAGON' 'Marca_GOMOTOR' 'Marca_GONOW' 'Marca_GREAT WALL MOTOR' 'Marca_GUZI' 'Marca_HAFEI' 'Marca_HAIMA' 'Marca_HAOJIANG' 'Marca_HAOJUE' 'Marca_HARLEY DAVIDSON' 'Marca_HERO' 'Marca_HIGER' 'Marca_HINO' 'Marca_HONDA' 'Marca_HONLEI' 'Marca_HUALIN' 'Marca_HUANGHAI' 'Marca_HUMMER' 'Marca_HUSQVARNA' 'Marca_HYOSUNG' 'Marca_HYUNDAI' 'Marca_INFINITI' 'Marca_INTERNATIONAL' 'Marca_ISUZU' 'Marca_IVECO' 'Marca_JAC' 'Marca_JAGUAR' 'Marca_JAWA' 'Marca_JEEP' 'Marca_JIALING' 'Marca_JINBEI' 'Marca_JINCHENG' 'Marca_JINFENG' 'Marca_JMC' 'Marca_JOYLONG' 'Marca_KAMAZ' 'Marca_KAWASAKI' 'Marca_KAYAK' 'Marca_KAZUKI' 'Marca_KEEWAY' 'Marca_KENWORTH' 'Marca_KIA' 'Marca_KTM' 'Marca_KYMCO' 'Marca_KYOTO' 'Marca_LADA' 'Marca_LANCIA' 'Marca_LAND ROVER' 'Marca_LANDWIND' 'Marca_LEXUS' 'Marca_LIFAN' 'Marca_LINCOLN' 'Marca_LML' 'Marca_LMX' 'Marca_MACK' 'Marca_MAHINDRA' 'Marca_MASERATI' 'Marca_MAXMOTOR' 'Marca_MAXUS' 'Marca_MAZDA' 'Marca_MD BIKES' 'Marca_MERCEDES BENZ' 'Marca_MERCURY' 'Marca_MG' 'Marca_MINI' 'Marca_MITSUBISHI' 'Marca_MORINI' 'Marca_MOTO ABC' 'Marca_MOTO GUZZI' 'Marca_MTK' 'Marca_MUDAN' 'Marca_MV AGUSTA' 'Marca_NISSAN' 'Marca_NITRO' 'Marca_NON PLUS ULTRA' 'Marca_OLTCIT' 'Marca_OPEL' 'Marca_PASSAGGIO' 'Marca_PEGASO' 'Marca_PEUGEOT' 'Marca_PIAGGIO' 'Marca_POLARIS' 'Marca_PONTIAC' 'Marca_PORSCHE' 'Marca_QINGQI' 'Marca_RENAULT' 'Marca_ROVER' 'Marca_ROYAL ENFIELD' 'Marca_SAAB' 'Marca_SACHS' 'Marca_SAICWULING' 'Marca_SANYA' 'Marca_SATURN' 'Marca_SCANIA' 'Marca_SCION' 'Marca_SCOMADI' 'Marca_SEAT' 'Marca_SHINERAY' 'Marca_SHUANGHUAN' 'Marca_SIGMA' 'Marca_SINOTRUK' 'Marca_SKODA' 'Marca_SKYGO' 'Marca_SMART' 'Marca_SMC' 'Marca_SOYAT' 'Marca_SSANGYONG' 'Marca_STEYR' 'Marca_SUBARU' 'Marca_SUKIDA' 'Marca_SUKYAMA' 'Marca_SUZUKI' 'Marca_SYM' 'Marca_T-KING' 'Marca_TATA' 'Marca_TEMPEST' 'Marca_TIANMA' 'Marca_TITANIA' 'Marca_TMD' 'Marca_TONGKO' 'Marca_TOYOTA' 'Marca_TRIUMPH' 'Marca_TVS' 'Marca_TX MOTORS' 'Marca_UFO' 'Marca_UKM' 'Marca_UNITED MOTORS' 'Marca_USW MOTORS' 'Marca_VERUCCI' 'Marca_VESPA' 'Marca_VICTORY' 'Marca_VOLKSWAGEN' 'Marca_VOLVO' 'Marca_WANXIN' 'Marca_WCR' 'Marca_XIANFENG' 'Marca_XINGYUE' 'Marca_XINKAI' 'Marca_YAKEY' 'Marca_YAKIMA' 'Marca_YAMAHA' 'Marca_YAXING' 'Marca_YINGANG' 'Marca_YUEJIN-NAVECO' 'Marca_YUGO' 'Marca_YUTONG' 'Marca_ZAHAV' 'Marca_ZHONGNENG' 'Marca_ZHONGXING' 'Marca_ZNA' 'Marca_ZONGSHEN' 'Marca_ZOTYE' 'Marca_ZQ MOTORS'
* 'Clase_BUS / BUSETA / MICROBUS' 'Clase_CAMION' 'Clase_CAMIONETA PASAJ.' 'Clase_CAMIONETA REPAR' 'Clase_CAMPERO' 'Clase_CARROTANQUE' 'Clase_CHASIS' 'Clase_FURGON' 'Clase_MOTOCARRO' 'Clase_MOTOCICLETA' Clase_PICKUP DOBLE CAB' 'Clase_PICKUP SENCILLA' 'Clase_REMOLCADOR' 'Clase_VOLQUETA'
* 'TipoCaja_MT' 'TipoCaja_TP'
* 'Nacionalidad_ARG' 'Nacionalidad_AUS' 'Nacionalidad_BRA' 'Nacionalidad_CAN' 'Nacionalidad_CHI' 'Nacionalidad_CHL' 'Nacionalidad_COL' 'Nacionalidad_CZE' 'Nacionalidad_ECU' 'Nacionalidad_ENG' 'Nacionalidad_ESP' 'Nacionalidad_FRA' 'Nacionalidad_HNG' 'Nacionalidad_IDN' 'Nacionalidad_IND' 'Nacionalidad_ITA' 'Nacionalidad_JAP' 'Nacionalidad_KOR' 'Nacionalidad_MEX' 'Nacionalidad_NED' 'Nacionalidad_RUM' 'Nacionalidad_RUS' 'Nacionalidad_SUE' 'Nacionalidad_TAI' 'Nacionalidad_TWN' 'Nacionalidad_USA' 'Nacionalidad_VEN'
* 'Combustible_GAS' 'Combustible_GSL' 'Combustible_HBD'
* 'Transmision_3X1' 'Transmision_3X2' 'Transmision_4X2' 'Transmision_4X4' 'Transmision_4x2' 'Transmision_6X2' 'Transmision_6X4' 'Transmision_6x4' 'Transmision_8X4'
* 'IdServicio'
* 'Importado'
* 'AireAcondicionado'
* 'CapacidadPasajeros'
* 'Puertas'
* 'Ejes'
* 'Peso'
* 'Potencia'
* 'Cilindraje'
* 'CapacidadCarga'

## Variable objetivo

La variable endógena que se busca estimar es: **Precio2018**

## Evaluación del modelo

### Métricas de evaluación

Debido a que se trata de un modelo de regresión utilizamos la métrica de ajuste *R^2*

### Resultados de evaluación

Tras realizar el entrenamiento del modelo y su respectiva evaluación obtuvimos un coeficiente de determinación *R^2* de 47.49%:

![Evaluación del modelo](image.png)

## Análisis de los resultados

Tras realizar el entrenamiento de este modelo base se obtiene un umbral que esperamos superar con futuras configuraciones y experimentos enfocados en las diversas opciones que tenemos de modificar la etapa de modelado para mejorar el rendimiento y la capacidad de predecir de nuestro modelo.

Un coeficiente de determinación *R^2* de casi 48% no está mal para empezar, sin embargo entre más logremos aumentar esta métrica mejor será el modelo que permitirá al negocio realizar las predicciones de precios de vehículos en Colombia.

Algunas de las etapas que avanzaremos en el futuro consistirán en:

1. Análisis de relevancia de las variables obtenidas tras el preprocesamiento dentro del modelo (Importancia de las características)
2. Análisis y optimización de hiperparámetros del modelo
3. Evaluación de otros posibles modelos de Regresión

## Conclusiones

Tras los resultados obtenidos se percibe un avance en la capacidad de predicción del precio de los vehículos en Colombia para el año 2018. Frente a la necedidad del negocio estamos obteniendo un 48% de ajuste del modelo frente a las estimaciones de precios, lo cual es positivo debida la complejidad del proyecto y refleja igualmente una buena selección de características iniciales en el proyecto. Las oportunidades de mejora fueron listadas anteriormente y esperamos poder aumentar la métrica pudiendo lograr un 70% de ajuste del modelo frente a los precios observados.
