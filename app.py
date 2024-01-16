import streamlit as st
from scscore.standalone_model_numpy import SCScorer
scscorer = SCScorer()
import rdkit.Chem as Chem
from rdkit.Chem import Draw
# Logo on top left
st.image('./catsci-logo.svg', width=200)  # Adjust width as needed

# Name of the script
st.title('SCR-02: SCScore')  # Replace with your script name

# Brief description
st.markdown('''
    This script provides a relative synthetic complexity of a molecule based on 12M reactions taken from Reaxys. The score ranges from 0 to 5, with higher values indicating a more challenging molecule.
    
    More information are in related paper [SCScore](https://pubs.acs.org/doi/10.1021/acs.jcim.7b00622)
    ''')

st.warning('For script you need input chirality specified SMILES, not any other [types](https://ics.uci.edu/~dock/manuals/DaylightTheoryManual/theory.smiles.html). Daylight SMILES type from ChemDoodle and isomeric type are required', icon="⚠️")

model = SCScorer()
model.restore()

molecule = st.text_input(' Please provide **Isomeric** SMILES')
(smi, score) = model.get_score_from_smi(molecule)
st.write('SCScore of input molecule %.3f' % (score))

m = Chem.MolFromSmiles(molecule)
img = Draw.MolToImage(m,size=(300,300))
st.image(img)

if score > 4.5:
    st.markdown("![Alt Text](https://media2.giphy.com/media/qjr1ZNLWEVvg9aFCyL/giphy.gif?cid=ecf05e47f71kjwwqvqv3e97308uh7hogs2jca3wlp5s0t1xd&ep=v1_gifs_search&rid=giphy.gif&ct=g)")
