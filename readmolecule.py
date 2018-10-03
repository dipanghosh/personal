node = hou.pwd()
geo = node.geometry()
#poly = geo.createPolygon()

import rdkit.Chem as ch
m = ch.SDMolSupplier("C:\\Users\\dipan\\Downloads\\\test.sdf")
mol = m[0]

atoms = mol.GetAtoms()
geo.addAttrib(hou.attribType.Point, "atomicNo", 0)
for atom_i in range(mol.GetNumAtoms()):
    posobj = mol.GetConformer().GetAtomPosition(atom_i)
    pos = hou.Vector3(posobj.x, posobj.y, posobj.z)
    pt = geo.createPoint()
    pt.setAttribValue("atomicNo",atoms[atom_i].GetAtomicNum())
    pt.setPosition(pos)
