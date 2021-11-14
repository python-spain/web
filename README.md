# Sitio web archivado
**:warning: La web actual no está en este repo, sino en [web-ng](https://github.com/python-spain/web-ng).**


# (antiguo) Sitio Web de la asociación Python España
> https://es.python.org

Este sitio web ha sido generado utilizando el generador de sitios web estáticos [Pelican](https://blog.getpelican.com/), escrito en Python.

El contenido está escrito en [Markdown](https://daringfireball.net/projects/markdown/syntax) y se encuentra localizado dentro de la carpeta [`contents`](https://github.com/python-spain/web/tree/master/content).

No necesitas conocimientos técnicos para añadir nuevo contenido a la web o editar el existente. Lee nuestra [guía de contribución](https://github.com/python-spain/web/tree/master/CONTRIBUTING.md) para aprender cómo proponer cambios desde el navegador.

Sin embargo, puedes [continuar leyendo](#prerrequisitos) si quieres probar el proyecto en un entorno de desarrollo local.

Recuerda que al participar en esta comunidad, aceptas y te comprometes a cumplir nuestro [código de conducta](https://github.com/python-spain/web/tree/master/CODE_OF_CONDUCT.md).

## Instalación del sitio web

### Clonando el repositorio

Comienza clonando el repositorio en tu entorno de desarrollo. Como el nombre del mismo es demasiado genérico, indica el directorio de destino como último parámetro:

```sh
$ git clone https://github.com/python-spain/web.git python-es-web
$ cd python-es-web
```

Para probar el sitio en local tienes dos opciones: usar docker o usar un entorno virtualenv.

### Usando docker

[Docker](https://docs.docker.com/) y [docker-compose](https://docs.docker.com/compose/) son herramientas que permiten generar entornos replicables y fáciles de compartir entre múltiples personas. Consulta [esta guía](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04) para instalar docker y docker-compose en un entorno Ubuntu. Para otros sistemas operativos, busca "cómo instalar docker-compose en (distribución/sistema operativo)".

Una vez instalado, ejecuta el siguiente comando dentro del directorio del proyecto para iniciar el servidor de desarrollo:

```sh
$ docker-compose up
```

Por defecto escuchará en `localhost:8000`. Las carpetas `themes` y `content` serán monitorizadas y el sitio web se regenerará automáticamente si el contenido cambia.


### Usando un virtualenv

#### Prerrequisitos

Probar el sitio web en local usando virtualenv requiere un entorno UNIX y los programas [`make`](https://www.gnu.org/software/make/), [`git`](https://git-scm.com/downloads), [`pip`](https://pip.pypa.io/en/stable/installing/) y [Python 2.7.x or 3.3+](https://www.python.org/downloads/). La siguiente guía asume que trabajas con Python 3.



#### Configuración del proyecto

> **NOTA**: Es opcional pero áltamente recomendable [trabajar en un entorno virtual de Python](#trabajar-en-un-entorno-virtual).

Las dependencias del sitio web se encuentran en el archivo `requirements.txt`. Instala las dependencias con `pip`:

```sh
$ pip install -r requirements.txt
```

##### Trabajar en un entorno virtual

Un [entorno virtual](https://docs.python.org/3/tutorial/venv.html) permite trabajar en un entorno Python 3 aislado e independiente de tu sistema. Esto quiere decir que los paquetes que instales dentro del entorno virtual no estarán disponibles en tu instalación global de Python o en otros entornos virtuales (y viceversa).

Para crear un entorno virtual, lanza el comando:

```sh
$ python3 -m venv venv
```

Para activar el entorno virtual, lanza el siguiente comando desde la raíz del repositorio:

```sh
$ source venv/bin/activate
```

Para salir de un entorno virtual activo, lanza el comando:

```sh
$ deactivate
```

#### Probando en local

Realiza pruebas en local lanzando el servidor de desarrollo:

```sh
$ make devserver
```

Por defecto, el servidor escucha en `http://localhost:8000`. Con este comando, las carpetas `themes` y `content` serán monitorizadas y el sitio web se regenerará automáticamente si el contenido cambia.

Si necesitas más información sobre los comandos de `make` que puedes utilizar, [consulta el manual de Pelican](http://docs.getpelican.com/en/stable/publish.html?highlight=make#make) o lanza el comando:

```sh
$ make
```

### Personalizaciones del estilo de la web

El tema de la web esta basado en el tema [Alchemy](https://github.com/nairobilug/pelican-alchemy#as-a-submodule) de Pelican.

Puedes aplicar ciertas modificaciones:

- en `themes/pelican-alchemy/alchemy/static/css/theme.css` puedes sobreescribir el estilo (al final del fichero hay un apartado para personalizaciones).
- en `themes/pelican-alchemy/alchemy/templates` encontrarás las plantillas.

