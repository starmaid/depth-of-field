# Blur Depth

This is a project to get crazy depth of field on an intel realsense or other depth camera.

This concept is just like a video game, where the depthbuffer is used to fake the optics.

I'm realizing that numpy and python don't have the shader capabilities that I need to do this. I can't be looping over every element in an image to do a simple pixel shader. I'm probably going to try webGL next, because that was already something I wanted to learn how to stream depth information to.

## Ref

[Acerola youtube video](https://www.youtube.com/watch?v=v9x_50czf-4)

[Acerola shader code](https://github.com/GarrettGunnell/AcerolaFX/blob/main/Shaders/AcerolaFX_BokehBlur.fx#L709)

[Damjan setting up a webcam](https://medium.com/docler-engineering/manipulating-video-in-a-browser-5b37f8149d9b)

[Damjan streaming video to webGL](https://medium.com/docler-engineering/webgl-video-manipulation-8d0892b565b6)

[aiortc example page](https://github.com/aiortc/aiortc/tree/main/examples/server)

[Lytro Illum Camera]()