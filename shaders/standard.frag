#version 130

#define MULT .05
#define OFFS -.1

uniform mat4 p3d_ViewProjectionMatrix;
uniform sampler2D p3d_Texture0;

in vec4 normal;
in vec2 texcoord;

vec4 sum(){
    float val = (max(abs(normal.x), abs(normal.y)) * MULT) + OFFS;
    return vec4(val, val, val, 0);
}

void main(){
    gl_FragColor = texture(p3d_Texture0, texcoord)-sum();
}