precision highp float;
varying vec3 P;
varying vec3 T;
varying vec3 C;
varying vec3 N;
varying vec3 L;
uniform mat4 ModelViewMatrix;
uniform mat4 NormalMatrix;
uniform vec3 CameraPos;
uniform sampler2D texture;
attribute vec3 p;
attribute vec3 t;
attribute vec3 n;
attribute vec3 c;
uniform float time;

void main()
{
  P = p;
  T = t;
  C = c;
  L = vec3(0,1,1);
  N = normalize(vec3(NormalMatrix*vec4(n,1)));	
  gl_Position = ModelViewMatrix * vec4(P,1);
}
