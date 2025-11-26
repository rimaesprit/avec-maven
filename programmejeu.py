print("=== 🎯 Jeu : Devine le nombre ! ===")
print("Je pense à un nombre entre 1 et 100...")

secret = 42  # tu peux changer la valeur ici
essais = 0

while True:
    reponse = input("👉 Entre ton nombre : ")

    # Vérifier si l’entrée est bien un nombre
    if not reponse.isdigit():
        print("⚠️ Entre un nombre valide !")
        continue

    reponse = int(reponse)
    essais += 1

    if reponse < secret:
        print("⬆️ Trop petit ! Essaie encore.")
    elif reponse > secret:
        print("⬇️ Trop grand ! Essaie encore.")
    else:
        print(f"🎉 Bravo ! Tu as trouvé en {essais} essais.")
        break
