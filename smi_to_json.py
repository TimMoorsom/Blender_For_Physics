import openbabel
from openbabel import pybel
import json

"""Insert smi string in place of C to convert. If smi fails, use InChi instead"""
molecule = pybel.readstring("Smi", "C")
molecule.make3D()

def molecule_to_json(molecule):
    """Converts an OpenBabel molecule to json for use in Blender."""

    # Save atom element type and 3D location.
    atoms = [{"element": atom.type,
              "location": atom.coords}
             for atom in molecule.atoms]

    # Save number of bonds and indices of endpoint atoms
    bonds = [{"atoms": [b.GetBeginAtom().GetIndex(), b.GetEndAtom().GetIndex()],
              "order": b.GetBondOrder()}
             for b in openbabel.OBMolBondIter(molecule.OBMol)]

    return json.dumps({"atoms": atoms, "bonds": bonds})

with open("phosphate-deoxyribose.json", "w") as out_file:
    out_file.write(molecule_to_json(molecule))
