🩺 veristream-x — Détection & Réfutation de Désinformation Médicale (BioBERT + RAG)
veristream-x est un système avancé conçu pour détecter, analyser et contrer la désinformation médicale dans tous les domaines de la santé : traitements, maladies, vaccins, médicaments, rumeurs scientifiques, mythes populaires, etc.

Il classe automatiquement toute affirmation comme fiable ou fausse, puis génère une réfutation scientifique, sourcée et pédagogique en cas de désinformation.

⭐ Résultats Clés
Précision (Accuracy) : 97.9 %

Score F1 : 97.9 %

Surapprentissage : très faible (écart train/val < 2 %)

Temps d'entraînement : ~30 minutes (GPU Colab T4)

Temps d'inférence : ~80 ms par texte

🚀 Fonctionnalités Principales
🧪 Détection Automatique
Classification binaire de n’importe quelle affirmation médicale.

🧠 Réfutation Intelligente
Génération de contre-arguments scientifiques, vérifiés et sourcés.

🔍 Analyse Contextuelle Avancée
Compréhension des formulations indirectes, vagues, informelles ou ambiguës.

🌐 Interface Utilisateur (Gradio)
Démonstration interactive simple et intuitive.

🧬 Architecture du Modèle
Modèle de Base
BioBERT, spécialisé dans le texte biomédical, pour une compréhension précise du langage médical.

Fine-Tuning
Dataset : 5 000 exemples équilibrés
— 3 500 entraînement
— 1 500 validation

Hyperparamètres :

4 époques

Batch size 16

Taux d’apprentissage 2e-5

Warmup 500 steps

Optimiseur : AdamW

Perte : CrossEntropyLoss

Régularisation : Dropout 0.3

🧠 Système de Contre-Argumentation (RAG-like)
1️⃣ Recherche
Extraction de contenus médicaux fiables dans une base vectorielle FAISS, construite à partir de :

organisations internationales de santé

agences de régulation

publications scientifiques

données publiques validées

2️⃣ Sélection
Récupération des top-3 passages les plus pertinents.

3️⃣ Génération des Réfutations
Utilisation de Llama-3.1 70B (Groq) pour produire des réponses :

claires

pédagogiques

scientifiquement valides

sourcées

4️⃣ Activation Automatique
Lorsque le modèle détecte une désinformation → le module RAG s’active automatiquement.

📈 Perspectives d’Évolution
Intégration d’une architecture Big Data complète :

Hadoop

Spark

Airflow

FAISS distribué

Augmentation automatique du dataset via collecte web continue.

Passage à des datasets massifs (100 000+ exemples).

Tableau de bord professionnel : Streamlit, Grafana.

Extension multimodale : analyse de textes + images (infographies, mèmes).

🏁 Conclusion
veristream-x est une solution moderne, robuste et extensible pour lutter contre la désinformation médicale.
Elle combine la puissance de BioBERT, la précision du fine-tuning et l’intelligence d’un module de contre-argumentation inspiré d’un RAG.

📜 Licence
MIT License — usage éducatif et recherche.
⚠️ Ce système ne remplace pas un avis médical professionnel
