# 🌟 Préparons notre environnement virtuel ! ✨
echo "=========================================================="
echo " 🌟 🔮 Création de l'environnement virtuel... ✨"
echo "=========================================================="
virtualenv ../.venv/

# Supprimons la base de donnée.
echo "=========================================================="
echo "🧹 Supprimons le db.sqlite3 ...  🧙‍♂️"
echo "=========================================================="
rm db.sqlite3

# 🚀 Installons toutes les dépendances ! 🧙‍♂️
echo "=========================================================="
echo "🚀🧹 Installation des dépendances magiques...  🧙‍♂️"
echo "=========================================================="
pip install -r requirements.txt

# 🏗️ Créons la magie des migrations! 🪄
echo "=========================================================="
echo "🏰 Création de la magie des migrations..."
echo "=========================================================="
python3 manage.py makemigrations

# 🌈 Appliquons la magie des migrations pour construire notre royaume enchanté! 🏰
echo "=========================================================="
echo "🌟 Application de la magie des migrations..."
echo "=========================================================="
python3 manage.py migrate

# 👑 Créons un super utilisateur avec des pouvoirs exceptionnels! 🦸‍♂️
echo "=========================================================="
echo "👑 Création d'un super utilisateur avec des pouvoirs exceptionnels..."
echo "=========================================================="
python3 manage.py createsuperuser --username amk

# 🎭 Exécutons le script de fabrication pour donner vie à nos rêves! 🌟
echo "=========================================================="
echo "🎭 Exécution du script de fabrication pour donner vie à nos rêves..."
echo "=========================================================="
python3 manage.py runscript seed