precision highp float;
uniform sampler2D texture;
uniform vec3 DiffuseColour;
varying vec3 P;
varying vec3 T;
varying vec3 C;
varying vec3 N;
varying vec3 L;

void main() {
    vec3 l = normalize(L);
    vec3 n = normalize(N);
    float diffuse = dot(vec3(0,1,1),n);

    gl_FragColor = vec4(texture2D(texture, vec2(T.s, T.t)).b*vec3(1.0,0.0,1.0), 
                        0.75*(1.0-texture2D(texture, vec2(T.s, T.t)).b));
}
