# -*- coding: utf-8 -*-
from pathlib import Path
from subprocess import Popen
from jinja2 import Template

FOAM_VERSION = "v2106"
FOAM_UTILS = Path(__file__).resolve().parent / "snippets"

with open(FOAM_UTILS / "foam_banner") as fp:
    FOAM_BANNER = fp.read()
    
with open(FOAM_UTILS / "foam_file") as fp:
    FOAM_FILE = fp.read()
    
with open(FOAM_UTILS / "foam_split") as fp:
    FOAM_SPLIT = fp.read()

with open(FOAM_UTILS / "foam_end") as fp:
    FOAM_END = fp.read()

FIELD_TYPES = {
    "scalar": "volScalarField",
    "vector": "volVectorField",
    "dict": "dictionary"
}

OBJECT_TYPES = {
    # zero
    "p": "volScalarField",
    "U": "volVectorField",
    "T": "volScalarField",

    # constant
    "combustionProperties": "dictionary",
    "chemistryProperties": "dictionary",
    "g": "uniformDimensionedVectorField",
    "initialConditions": "dictionary",
    "thermophysicalProperties": "dictionary",
    "transportProperties": "dictionary",
    "turbulenceProperties": "dictionary",
    
    # system
    "controlDict": "dictionary",
    "decomposeParDict": "dictionary",
    "fvSchemes": "dictionary",
    "fvSolution": "dictionary",

    # system (non-standard)
    "foamDataToFluentDict": "dictionary"
}


def make_header(object_name, class_type, force_type=False):
    """ Compose file header for class type/given object. """
    if force_type:
        class_name = class_type
    elif class_type is not None and class_type in FIELD_TYPES:
        class_name = FIELD_TYPES[class_type]
    else:
        class_name = OBJECT_TYPES[object_name]

    foam_banner = FOAM_BANNER.replace("xxxxx", FOAM_VERSION[:5])
    foam_file = FOAM_FILE.format(class_name=class_name,
                                 object_name=object_name)
    foam_head = f"{foam_banner}\n{foam_file}\n{FOAM_SPLIT}\n"
    return foam_head


def make_file(case, loc, fname, body, class_type=None, force_type=False):
    """ Prepare contents and dump in case at given location. """
    loc = Path(case) / loc
    loc.mkdir(exist_ok=True, parents=True)

    with open(loc / fname, "w") as fp:
        head = make_header(fname, class_type, force_type)
        fp.write(f"{head}\n{body}\n\n{FOAM_END}\n")


def run_cmd(case, logname, command):
    """ Run command from case directory. """
    with open(f"{case}/{logname}", "w") as output:
        print(f"Running from {case}")
        server = Popen(command, cwd=case, shell=True,
                       stdout=output, stderr=output)
        server.communicate()

        
def boundary_fields_template(boundaries):
    """ Create a template from a set of names. """
    # TODO move this to file.
    baseBoundaryField = Template("""\
    dimensions      {% raw %}{{ {% endraw %}dimensions{% raw %} }}{% endraw %};

    internalField   uniform {% raw %}{{ {% endraw %}uniform{% raw %} }}{% endraw %};

    boundaryField
    {
        {% for patch in boundaries %}
        {{ patch }}
        {
    {% raw %}{{ {% endraw %}{{ patch }}{% raw %} }}{% endraw %}
        }
        {% endfor %}
    }
    """)
    
    return Template(baseBoundaryField.render(boundaries=boundaries))


