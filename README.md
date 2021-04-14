# Extraccion-de-fondo

[Spanish]
Detector de movimiento basado en la extracción del fondo.
Se establece una primera imagen de referencia sobre la que realizar comparaciones. Cunado se obtiene una nueva imagen de 
la cámara la comparación entre la imagen de referencia y la nueva imagen determinará si existe movimiento o no. Para eliminar 
posible ruido tanto la imagen de referencia como las nuevas imágenes se transforman a gris. Si se quiere evitar aún más ruido, 
una opción es aplicar un filtro a la nueva imagen que haga que esta sea más borrosa de lo normal. Posteriormente se comparan las 
dos imágenes píxel a píxel y, en función de un umbral establecido, se obtiene una nueva imagen con píxeles blancos y negros. 
Normalmente los píxeles blancos son asignados a aquellos píxeles que superan cierto umbral, es decir, se trata de aquellos píxeles 
que podrían ser considerados movimiento. Los píxeles negros representan lo contrario. Una vez que se han obtenido dichos píxeles es 
necesario determinar si se ha producido movimiento o no. Si contásemos la cantidad total de píxeles blancos podríamos generar falsos 
positivos por culpa del ruido, el mismo podría estar generando ciertos píxeles aislados. La solución reside en establecer un número 
mínimo píxeles blancos consecutivos, también llamado borde.   

[English]
Motion detector based on the extraction of the bottom. A first reference image is established on which you make comparisons. When 
you get a new image of the camera the comparison between the reference image and the new image will determine if there is movement 
or not. To remove possible noise both the reference image and the new images are grayed out. If you want to avoid even more noise,
One option is to apply a filter to the new image that makes it more blurry than normal. Subsequently, the two images pixel by pixel 
and, based on a set threshold, a new image is obtained with black and white pixels. Normally the white pixels are assigned to those 
pixels that exceed a certain threshold, that is, they are those pixels that could be movement relevant. Black pixels represent the 
opposite. Once these pixels have been obtained it is It is necessary to determine whether movement has occurred or not. If we counted 
the total amount of white pixels we could generate false positive due to noise, it could be generating certain isolated pixels. The 
solution lies in setting a number minimum consecutive white pixels, also called border.
