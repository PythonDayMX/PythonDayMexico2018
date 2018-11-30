
![BANNER](./repo-img/Banner.png)

## Descripción
Twitch es una de las plataformas de live streaming que más ha crecido en los últimos años. Todos los días, millones de personas se conectan a la plataforma con el objetivo de buscar entrenerse, mejorar sus habilidades al jugar videojuegos, interactuar con su comunidad nicho, entre otros objetivos ([Sjöblom, Max et. al](https://www.researchgate.net/publication/311235384_Why_do_people_watch_others_play_video_games_An_empirical_study_on_the_motivations_of_Twitch_users)).

Es por esto que el estudio de la plataforma en estudios _Interacción Humano Computadora_ se ha convertido de interés ya que nos permite entender a profunidad los motivos y medios por los que la gente utiliza este tipo de plataformas así como comprender a profundidad el comportamiento de su audiencia, streamers y moderadores ([Seering, Joseph et. al](https://dl.acm.org/citation.cfm?id=3274426)). Finalmente, esto nos ayuda a entender como utilizamos este tipo de medios digitales y establecer propuestas de diseño para mejorar las interacciones y experiencias de los usuarios.

### Objetivos
En este workshop buscamos:
 - Explorar las oportunidades en investigación y desarrollo que tiene la construccion de bots en Twitch.
 - Construcción de un Bot que se conecté a un canal en Twitch.
 - Crear interacciones con el bot.

## Instalación
1. Clona el repositorio
```git
git clone https://github.com/PythonDayMX/PythonDayMexico2018.git

cd PythonDayMexico2018/IntroABotsEnTwitch
```
2. [Inicia sesión](https://www.twitch.tv/login) en Twitch o [crea una cuenta](https://www.twitch.tv/signup) nueva.
3. Consigue tu Twitch Chat OAuth Token en esta [página](http://twitchapps.com/tmi/)
4. Agrega tu oauth token a el archivo `_settings.py` y cambia el nombre a `settings.py` (solo quita el `_`).
5. Instala los modulos necesarios `pip install -r requirements.txt`


## Ejecución
¡Ejecuta `python bots.py` y listo!

## Cómo Contribuir
¿Nos hace falta algo?¿Hay algún error? Si notas que hay algún error en el repositorio puedes crear un ISSUE nuevo para que lo corrijamos o mejor aún ayudarnos con un PULL REQUEST :tada:. Si es la primera vez que contribuyes a un proyecto no dudes en hacernos preguntas sobre como contribuir.

1. Haz un fork del repositorio
2. Crea una rama con la funcionalidad que vas a agregar: `git checkout -b my-new-feature`
3. Guarda tus cambios: `git commit -am 'Add some feature'`
4. Sube tu rama a tu fork: `git push origin my-new-feature`
5. ¡Crea un Pull Request y listo! :octocat:

## Creditos
- Juan Pablo Flores [:octocat:](github.com/juanpflores)

## Licencia
Este proyecto cuenta con una Licencia GNU GENERAL PUBLIC LICENSE. Puedes revisar los detalles de la licencia en este [documento](LICENSE)