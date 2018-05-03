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
  vec4 wp = ModelViewMatrix * vec4(0,0,0,1);
  vec4 push = texture2D(texture, vec2(wp.x+time*10.0, wp.y+time*1.0)*0.01);

  P = vec3(p.x+(push.r-0.5),
	   p.y+(push.g-0.5),
	   p.z);
  T = t;
  C = c;
  L = vec3(0,1,1); /* vec3(ModelViewMatrix*vec4((vec3(0,10,0)-p),1)); */
  N = normalize(vec3(NormalMatrix*vec4(n,1)));	
  gl_Position = ModelViewMatrix * vec4(P,1);
}
