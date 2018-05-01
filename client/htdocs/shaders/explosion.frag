precision highp float;
uniform sampler2D texture;
uniform vec3 DiffuseColour;
varying vec3 P;
varying vec3 T;
varying vec3 C;
varying vec3 N;
varying vec3 L;

void main() {
  gl_FragColor = vec4(DiffuseColour,1.0);
}
