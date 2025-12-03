veristream-x
🩺 Détecteur de Désinformation Médicale
Description
veristream-x est un système avancé de détection de désinformation médicale, conçu pour identifier les fausses affirmations liées à la santé — en particulier autour du COVID-19 et des vaccins.

Le projet repose sur :

BioBERT, un modèle BERT spécialisé dans le domaine biomédical.

Un fine-tuning pour classer les textes en information fiable (classe 0) ou désinformation (classe 1).

Un module avancé de contre-argumentation inspiré du RAG, capable de récupérer des informations issues de sources fiables (OMS, CDC, EMA…) pour générer des réfutations factuelles et pédagogiques.

Le dataset final utilisé pour l’entraînement contient 5000 exemples équilibrés (50% vrais / 50% fake), issus d’un dataset Kaggle sur les fake news COVID enrichi par des augmentations permettant de varier les styles (formel, informel, question, message social, etc.).

Fonctionnalités Principales
Détection Automatisée
Classification binaire des affirmations médicales avec une précision dépassant 97% sur le set de validation.

Fine-Tuning BioBERT
Fine-tuning sur 4 epochs, batch 16, learning rate 2e-5, régularisation via dropout et AdamW.

Contre-Argumentation RAG-like
Récupération d’informations fiables via FAISS + génération d'une réfutation sourcée via Llama-3.1 (Groq).

Analyse Intelligente
Extraction automatique du contenu d'une rumeur même si la phrase est indirecte :
"J’ai entendu que les vaccins changent l’ADN…" → extraction sémantique → analyse correcte.

Robustesse
Testé sur des cas extrêmes, ambigus ou très courts avec excellente stabilité.

Interface Gradio
Une interface utilisateur simple permettant de tester le modèle et d’afficher la contre-argumentation.

Installation
Cloner le repository :

git clone https://github.com/votre-repo/medical-misinfo-detector.git
cd medical-misinfo-detector
Installer les dépendances :

pip install torch transformers sentence-transformers faiss-cpu gradio groq requests beautifulsoup4
Ajouter la clé API Groq pour la contre-argumentation :

Télécharger le modèle fine-tuné disponible dans /models/medical_fake_news_model.zip et le dézipper.

Utilisation
Détection simple : donne le verdict (réel/fake) + confiance.

Détection + Contre-Argumentation : renvoie la classification et une réfutation sourcée générée à partir des documents les plus pertinents du corpus fiable.

Interface web : lancement de l’interface Gradio pour tester le système.

Détails du Modèle et Fine-Tuning
Modèle de Base
BioBERT, embeddings 768 dimensions.

Architecture globale
BioBERT pour l’encodage.

Une couche linéaire permettant d’intégrer des features additionnelles.

Un classificateur dense à deux couches.

Dropout 0.3 pour éviter l’overfitting.

Paramètres d’entraînement
Dataset : 5000 exemples (3500 train / 1500 validation).

4 epochs, batch 16.

Learning rate 2e-5, warmup 500 steps.

Optimiseur AdamW.

Perte : CrossEntropyLoss.

Résultats
Accuracy validation : 97.9%

F1-score : 97.9%

Overfitting très faible (écart < 2%).

Entraînement effectué en ~30 minutes sur GPU (Colab/T4).

Contre-Argumentation via Système RAG
Le module de réfutation suit une logique inspirée des architectures RAG :

1. Retrieval
Recherche dans une base vectorielle FAISS construite à partir de pages fiables (OMS, CDC, EMA…).

Découpage en chunks (~1000 caractères).

2. Augmentation
Récupération des 3 chunks les plus pertinents (top-k = 3).

Injection dans le prompt du modèle Llama-3.1 via Groq.

3. Génération
Production d’une réfutation :

claire

pédagogique

sourcée

scientifiquement correcte

4. Intégration
Si le texte est détecté comme fake, le module RAG est automatiquement déclenché.

Perspectives et Évolutions Futures
Le projet sera étendu pour intégrer :

Une architecture Big Data complète (Hadoop / Spark / Airflow).

Un pipeline distribué pour :

la collecte massive de nouvelles sources médicales,

le nettoyage et prétraitement,

la génération continue d’embeddings,

la mise à jour automatique de la base FAISS.

Un entraînement scalable afin de gérer des datasets beaucoup plus vastes (100k+, 1M+ exemples).

Un tableau de bord de monitoring (via Streamlit ou Grafana).

Un module de détection multimodale (texte + image).

Cette évolution vise à rendre veristream-x totalement scalable, modulable et déployable en environnement industrie

