# Importer les fonctions nécessaires depuis les fichiers correspondants
from dates import extract_dates_from_table
from montant import extract_and_display_subvention_amount
from avis import extract_and_format_specific_info

# Fichier PowerPoint
pptx_file_path = 'Exemple FASEP.pptx'

# Diapositive 3, Tableau 1
slide_index_dates = 3
table_index_dates = 1
labels_dates = ["Date de signature", "Montant et date de paiement de l'acompte"]

# Diapositive 1, Tableau 2
slide_index_montant = 1
table_index_montant = 2
labels_montant = "Montant du FASEP"

# Diapositive 4, Tableau 1
slide_index_avis = 4
table_index_avis = 1
labels_avis = "Avis sur le versement intermédiaire"

# ...

# Extraction des dates
dates_result = extract_dates_from_table(pptx_file_path, slide_index_dates, table_index_dates, labels_dates)
if dates_result:
    print(f"Dates de signature de la convention de don pour la subvention: {dates_result}")

# Extraction du montant de la subvention
montant_result = extract_and_display_subvention_amount(pptx_file_path, slide_index_montant, table_index_montant, labels_montant)
if montant_result:
    print(f"Montant du FASEP: {montant_result}")

# Extraction de l'avis
avis_result = extract_and_format_specific_info(pptx_file_path, slide_index_avis, table_index_avis, labels_avis)
if avis_result:
    print(f"Avis sur le versement intermédiaire: {avis_result}")
