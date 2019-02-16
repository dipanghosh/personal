node = hou.pwd()
geo = node.geometry()

geo.addAttrib(hou.attribType.Point, "atomindex", 0)
geo.addAttrib(hou.attribType.Point, "atomname", "A")
geo.addAttrib(hou.attribType.Point, "resi", "A")
geo.addAttrib(hou.attribType.Point, "chain", "A")
geo.addAttrib(hou.attribType.Point, "resiN", 0)
geo.addAttrib(hou.attribType.Point, "atomtype", "A")

def readPDB(inFile):
    """
    This function will read "inFile" andw glean the
    position and atom attribs, if any, from it.

    """
    # a typical PDB lines has:
    # atomtag, id, atomname, resi, chain, resiN, posX,posY,posZ, bf, _junk, atomtype
    #
    atomtag, id, atomname, resi, chain, resiN, posX, posY, posZ, bf, _junk, atomtype = range(12)

    thePDB = open(inFile, 'r').readlines()

    atomattribs = []

    for l in thePDB:
        tokens = l.split()
        if len(tokens) != 12:
            continue
        if tokens[atomtag] == "ATOM":
            atomattribs.append(tokens[1:])

    return atomattribs

def createpoints(atomattribs):
    for atom in atomattribs:
        id, atomname, resi, chain, resiN, posX, posY, posZ, bf, _junk, atomtype = atom
        pos = hou.Vector3(float(posX), float(posY), float(posZ))
        pt = geo.createPoint()
        pt.setPosition(pos)
        pt.setAttribValue("atomindex",int(id))
        pt.setAttribValue("atomname",str(atomname))
        pt.setAttribValue("resi",str(resi))
        pt.setAttribValue("chain",str(chain))
        pt.setAttribValue("resiN",int(resiN))
        pt.setAttribValue("atomtype",str(atomtype))

pdbfile = "C:\\Users\\Dipan\\Documents\\\4e5d.pdb"

atomattribs = readPDB(pdbfile)

createpoints(atomattribs)
