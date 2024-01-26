# Blur Depth

This is a project to get crazy depth of field on an intel realsense or other depth camera.

This concept is just like a video game, where the depthbuffer is used to fake the optics.

I'm realizing that numpy and python don't have the shader capabilities that I need to do this. I can't be looping over every element in an image to do a simple pixel shader. I'm probably going to try webGL next, because that was already something I wanted to learn how to stream depth information to.

## set up

```
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## New idea

do it in post after taking a photo. Gstreamer and openCV RTSP or WebRTC streams are hell on windows.



## Ref

[Acerola youtube video](https://www.youtube.com/watch?v=v9x_50czf-4)

[Acerola shader code](https://github.com/GarrettGunnell/AcerolaFX/blob/main/Shaders/AcerolaFX_BokehBlur.fx#L709)

[Damjan setting up a webcam](https://medium.com/docler-engineering/manipulating-video-in-a-browser-5b37f8149d9b)

[Damjan streaming video to webGL](https://medium.com/docler-engineering/webgl-video-manipulation-8d0892b565b6)

[aiortc example page](https://github.com/aiortc/aiortc/tree/main/examples/server)

[Lytro Illum Camera]()


https://gstreamer.freedesktop.org/documentation/opengl/glshader.html?gi-language=python#glshader



## Gstreamer

https://www.youtube.com/watch?v=HDY8pf-b1nA&t=405s

https://gitlab.freedesktop.org/gstreamer/gstreamer/-/tree/main

https://fluendo.com/en/blog/gstreamer-python-bindings-for-windows/

fuick this software. AUGH WHY PYTHON BINDINGS SO HARD ON WINDOWS. I SHOULD JUST DO THIS ON LINUX BUT I WANT TO USE MY PWOERFUL COMPUTER. AND FUCKING CMON

git clone https://gitlab.freedesktop.org/gstreamer/gstreamer.git

git checkout tags/1.22.9

meson setup build -Dintrospection=enabled --prefix c:/gstreamer-python

meson setup --vsenv builddir

it cant find `g-ir-scanner` so fml. back to aiortc

meson compile -C builddir

