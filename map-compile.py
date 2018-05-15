import json
import base64

# stuff all the scheme code into the ditto js file
# so that it can be loaded locally

pre = "map-pre.html"
target = "map.html"

# more time and I would go through searching for loads to
# do this automatically - todo
code = ["scm/map/map.jscm"]

frames = [
"bend 1 red.png",
"bend 2 red.png",
"bend 3 red.png",
"bend 4 red.png",
"bend 5 red.png",
"bend 6 red.png",
"bend knees black.png",
"bend knees red.png",
"jump 1 black.png",
"jump 2 black.png",
"jump 3 black.png",
"jump 4 black.png",
"jump 5 black.png",
"jump 6 black.png",
"pat head 1 red.png",
"pat head 2 red.png",
"pat head 3 red.png",
"pat head 4 red.png",
"pat head 5 red.png",
"pat head bend knees black.png",
"scratch head 1 black.png",
"scratch head 2 black.png",
"scratch head 3 black.png",
"start black.png",
"start red.png",
"tap foot black.png",
"walk 10 black.png",
"walk 11 black.png",
"walk 12 black.png",
"walk 13 black.png",
"walk 14 black.png",
"walk 15 black.png",
"walk 16 black.png",
"walk 17 black.png",
"walk 18 black.png",
"walk 19 black.png",
"walk 1 black.png",
"walk 20 black.png",
"walk 21 black.png",
"walk 22 black.png",
"walk 23 black.png",
"walk 24 black.png",
"walk 25 black.png",
"walk 26 black.png",
"walk 27 black.png",
"walk 2 black.png",
"walk 3 black.png",
"walk 4 black.png",
"walk 5 black.png",
"walk 6 black.png",
"walk 7 black.png",
"walk 8 black.png",
"walk 9 black.png",
"yogi 1 black.png",
"yogi 1 red.png",
"yogi 2 black.png",
"yogi 2 red.png",
]

def prep_frame(f):
    return "textures/frames/"+f

resources = [ 
    "flx/scm/base.jscm",
    "flx/scm/maths.jscm",
    "flx/scm/glsl.jscm",
    "flx/scm/state.jscm",
    "flx/scm/pdata.jscm",
    "flx/scm/scenegraph.jscm",
    "flx/scm/primitive.jscm",
    "flx/scm/data.jscm",
    "flx/scm/shaders.jscm",
    "flx/scm/renderer.jscm",
    "flx/scm/instanceprim.jscm",
    "flx/scm/polyprim.jscm",
    "flx/scm/geometry.jscm",
    "flx/scm/texture.jscm",
    "flx/scm/meshcache.jscm",
    "flx/scm/shadercache.jscm",
    "flx/scm/fluxus.jscm",
    
    "flx/scm/canvas.jscm",
    "flx/scm/canvas-widgets.jscm",

    "scm/map/anim.jscm",
    
    "shaders/default.vert",
    "shaders/default.frag",
    "shaders/person.vert",
    "shaders/person.frag",

    "textures/white.png",
    "textures/map-exclusion.png",
    "textures/map-zones.png",
    "textures/char-start.png",
    "textures/char-red.png",

    "models/circlefan.obj",
    "models/plane.obj",
]+map(prep_frame,frames)

################################################

def load_from_file(fn):
    with open(fn, 'r') as myfile:
        return myfile.read()

def load_from_files(fnl):
    ret = ""
    for fn in fnl:
        ret+=load_from_file(fn)
    return ret

def base64_from_file(fn):
    with open(fn, "rb") as f:
        return base64.b64encode(f.read())
        
def insert_code(target_data,target,scm):
    scm = scm.replace("\n","\\n\\\n")
    scm = scm.replace("'","\\'")
    return target_data.replace(target,scm)

def build_resources(resource_files):
    res = {}
    for fn in resource_files:
        if fn.endswith(".png") or fn.endswith(".jpg"):
            res[fn]=base64_from_file(fn)
        else:
            res[fn]=load_from_file(fn)
    return json.dumps(res)

###################################################

pre_data=load_from_file(pre)
target_data=pre_data

target_data=insert_code(target_data,"{{SYNTAX}}",load_from_file("flx/scm/syntax.jscm"))
target_data=insert_code(target_data,"{{CODE}}",load_from_files(code))
target_data=insert_code(target_data,"{{RESOURCES}}",build_resources(resources))

with open(target, 'w') as myfile:
    myfile.write(target_data)

