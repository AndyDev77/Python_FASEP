## 📋 <a name="table">Projet FASEP</a>

1.  [Introduction](#introduction)
2.  🤖 [Configuration](#configuration)
3.  🤸 [Utilisation](#utilisation)
4.  ⚙️ [Fonctions principales](#tech-stack)
5.  🔋 [Tests](#tests)
6.  🕸️ [Remarques](#remarques)

## <a name="introduction">Introduction</a>

Ce projet permet d'extraire des informations spécifiques à partir d'un fichier PowerPoint (.pptx). Actuellement, il prend en charge l'extraction des dates de signature de la convention de don pour la subvention, le montant de la subvention du fonds d’étude et d’aide au secteur privé (FASEP) et de t l’avis du service économique de l’ambassade pour le premier terme intermédiaire de la subvention à partir de certaines diapositives et tableaux spécifiques.

## <a name="configuration">🤖 Configuration</a>

Avant d'utiliser le projet, assurez-vous d'avoir les dépendances nécessaires installées. Vous pouvez les installer en utilisant la commande suivante :

```bash
pip install -r requirements.txt

```

## <a name="utilisation">🤸 Utilisation</a>

1. Configuration : Assurez-vous que le fichier PowerPoint que vous souhaitez traiter est spécifié dans le fichier main.py. Modifiez la variable pptx_file_path avec le chemin approprié.

2. Exécutez le script principal main.py en utilisant la commande suivante dans votre terminal :

```bash
python main.py

```

3. Résultats : Le script affichera les résultats de l'extraction des dates, du montant et de l'avis à partir des diapositives spécifiées.

## <a name="tech-stack">⚙️ Fonctions principales</a>

👉 **extract_dates_from_table(slide_index, table_index, labels_to_extract) :** Cette fonction extrait les dates d'une table spécifiée sur une diapositive donnée.

- slide_index:\*\* L'indice de la diapositive.
- table_index:\*\* L'indice du tableau sur la diapositive.
- labels_to_extract:\*\* Liste des libellés à extraire.

👉 **extract_montant_from_table(slide_index, table_index, target_label) :** Cette fonction extrait le montant d'un tableau spécifié sur une diapositive donnée.

- slide_index:\*\* L'indice de la diapositive.
- table_index:\*\* L'indice du tableau sur la diapositive.
- target_label:\*\* Libellé du montant à extraire.

👉 **extract_montant_from_table(slide_index, table_index, target_label) :** Cette fonction extrait l'avis d'un tableau spécifié sur une diapositive donnée.

- slide_index:\*\* L'indice de la diapositive.
- table_index:\*\* L'indice du tableau sur la diapositive.
- target_label:\*\* Libellé de l'avis à extraire.

## <a name="tests">🔋 Tests</a>

Les tests unitaires pour les fonctions principales sont inclus dans le répertoire tests/. Vous pouvez les exécuter à l'aide de la commande suivante :

```bash
python -m unittest discover tests

```

## <a name="remarques">Remarques</a>

- Ce projet est actuellement conçu pour des fichiers PowerPoint spécifiques. Assurez-vous que la structure des diapositives et des tableaux correspond à celle attendue par le script.

- Les résultats de l'extraction seront affichés dans la console.
