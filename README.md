veristream-x est un système avancé conçu pour détecter et contrer la désinformation médicale, avec un focus particulier sur le COVID-19 et les vaccins. Il analyse automatiquement les affirmations pour les classer comme fiables ou fausses, et génère des réfutations factuelles et sourcées en cas de désinformation.

Résultats Clés
Précision : 97.9 % sur le jeu de validation
Score F1 : 97.9 %
Surapprentissage : Très faible (écart train/validation < 2 %)
Temps d'entraînement : Environ 30 minutes sur GPU (Colab T4)
Temps d'inférence : ~80 ms par texte
Fonctionnalités Principales
Détection Automatique : Classification binaire précise des affirmations médicales.
Réfutation Intelligente : Génération de contre-arguments sourcés et pédagogiques.
Gestion Contextuelle : Analyse efficace de formulations variées (directes, indirectes, informelles).
Interface Utilisateur : Démonstration interactive via Gradio.
Architecture du Modèle
Base : BioBERT (adapté au domaine biomédical).
Fine-Tuning :
Dataset : 5 000 exemples équilibrés (3 500 entraînement / 1 500 validation).
Hyperparamètres : 4 époques, batch size 16, taux d'apprentissage 2e-5, warmup 500 steps.
Optimiseur : AdamW.
Perte : CrossEntropyLoss.
Régularisation : Dropout 0.3 pour éviter le surapprentissage.
Système de Contre-Argumentation (Inspiré RAG)
Recherche : Extraction de chunks pertinents (1 000 caractères) d'une base vectorielle FAISS construite à partir de sources officielles (OMS, CDC, EMA).
Augmentation : Sélection des 3 chunks les plus similaires.
Génération : Utilisation de Llama-3.1 70B (via Groq) pour produire une réfutation claire, sourcée et pédagogique.
Intégration : Activation automatique en cas de détection de désinformation.
Perspectives d'Évolution
Pipeline Big Data scalable (Hadoop, Spark, Airflow).
Collecte et mise à jour automatique de sources médicales.
Entraînement sur des datasets étendus (100 000+ exemples).
Tableau de bord de monitoring (Streamlit ou Grafana).
Extension multimodale (texte + images/mèmes).
veristream-x est prêt pour un déploiement industriel, offrant une solution fiable et évolutive contre la désinformation médicale.

Licence : MIT. À usage éducatif et de recherche uniquement. Consultez toujours un professionnel de santé pour des conseils médicaux.


