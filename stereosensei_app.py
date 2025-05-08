
import streamlit as st
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem

# Page config
st.set_page_config(page_title="Stereosensei", layout="wide")

st.title("Stereosensei")

# Sidebar controls
st.sidebar.header("Viewer Controls")
bg_color = st.sidebar.selectbox("Background Color", ["white", "black", "gray"])
show_atom_labels = st.sidebar.checkbox("Show Atom Labels", value=False)
highlight_chiral = st.sidebar.button("Highlight Chiral Centers")
reset_view = st.sidebar.button("Reset View")

# Example molecules
molecules = {
    "2-Butanol (R)": "CC(C)CO",
    "2-Butanol (S)": "CC(C)CO",
    "Maleic Acid (cis)": "OC(=O)C=CC(=O)O",
    "Fumaric Acid (trans)": "OC(=O)C=CC(=O)O"
}
selected = st.selectbox("Select a Molecule:", list(molecules.keys()))
smiles = molecules[selected]

# RDKit molecule setup
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, AllChem.ETKDG())

# Convert to MolBlock for 3Dmol viewer
mol_block = Chem.MolToMolBlock(mol)

# Py3Dmol viewer
view = py3Dmol.view(width=600, height=500)
view.addModel(mol_block, "mol")
style = {"stick": {}}
if show_atom_labels:
    style["label"] = {"fontSize": 10, "position": "auto"}
view.setStyle(style)
view.setBackgroundColor(bg_color)
view.zoomTo()

# Render 3D viewer
st.components.v1.html(view.render(), height=500, scrolling=False)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Created by Dr. Walton</div>", unsafe_allow_html=True)
