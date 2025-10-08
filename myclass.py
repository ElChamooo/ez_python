import math

class Noe:
    def __init__(self, name, age, profession,default_color):
        """
        Constructeur de la classe Noe.
        :param name: Nom de la personne.
        :param age: Âge de la personne.
        :param profession: Profession de la personne.
        """
        self.name = name
        self.age = age
        self.profession = profession
        self.default_color=default_color
        self.color=default_color

    def introduce(self):
        """
        Retourne une introduction de la personne.
        """
        return f"Bonjour, je m'appelle {self.name}, j'ai {self.age} ans et je suis {self.profession}."

    def celebrate_birthday(self):
        """
        Incrémente l'âge de la personne d'une année.
        """
        self.age += 1
        return f"Joyeux anniversaire {self.name} ! Vous avez maintenant {self.age} ans."

    def change_profession(self, new_profession):
        """
        Change la profession de la personne.
        :param new_profession: Nouvelle profession.
        """
        self.profession = new_profession
        return f"{self.name} est maintenant {self.profession}."
    
    def go_tanning(self, time):
        """
        Simule une séance de bronzage.
        La couleur devient plus foncée proportionnellement à la durée.
        :param time: Durée de la séance en minutes.
        """
        # paramètres de contrôle
        max_minutes = 180               # durée après laquelle l'assombrissement atteint son maximum
        max_darkening = 0.7            # fraction maximale d'assombrissement (0 = aucune, 1 = noir)

        # couleur de base (par défaut si format invalide)
        hex_color = (self.default_color or "#FFFFFF").lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join(c*2 for c in hex_color)

        try:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
        except Exception:
            r, g, b = 255, 255, 255

        # facteur entre 0 et 1 proportionnel au temps
        factor = max(0.0, min(float(time) / max_minutes, 1.0))
        darkening = max_darkening * factor

        # appliquer l'assombrissement (réduction linéaire de la luminosité)
        new_r = int(r * (1.0 - darkening))
        new_g = int(g * (1.0 - darkening))
        new_b = int(b * (1.0 - darkening))

        self.color = f"#{new_r:02X}{new_g:02X}{new_b:02X}"
        return f"Après {time} minutes au soleil, {self.name} est maintenant de couleur {self.color}."
    
    def natural_untanning(self, time):
        """
        Débronzage naturel non-linéaire en fonction du temps (minutes).
        Le débronzage est plus rapide lorsque la couleur actuelle est plus éloignée
        de la couleur par défaut (plus bronzé -> récupération plus rapide).
        Retourne un message avec la nouvelle couleur et le pourcentage de récupération.
        """
        time = max(0.0, float(time))

        def _parse_hex(h):
            if not h:
                h = "#FFFFFF"
            h = h.lstrip('#')
            if len(h) == 3:
                h = ''.join(c*2 for c in h)
            try:
                return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
            except Exception:
                return 255, 255, 255

        cur_r, cur_g, cur_b = _parse_hex(self.color)
        def_r, def_g, def_b = _parse_hex(self.default_color)

        # distance euclidienne normalisée entre couleur actuelle et couleur par défaut
        dr = cur_r - def_r
        dg = cur_g - def_g
        db = cur_b - def_b
        dist = math.sqrt(dr*dr + dg*dg + db*db)
        max_dist = math.sqrt(3 * (255**2))
        dist_norm = dist / max_dist  # dans [0,1], 0 = déjà à la couleur par défaut

        # modèle non-linéaire : récupération exponentielle avec un taux qui augmente
        # quand la personne est plus bronzée (dist_norm plus grand).
        base_rate = 0.01      # taux de récupération de base (ajuster si besoin)
        sensitivity = 2.0     # combien le taux augmente selon le bronzage
        rate = base_rate * (1.0 + sensitivity * dist_norm)

        # fraction de récupération vers la couleur par défaut (0..1)
        recovered_frac = 1.0 - math.exp(-rate * time)
        recovered_frac = max(0.0, min(recovered_frac, 1.0))

        # appliquer la récupération : déplacer la couleur actuelle vers la couleur par défaut
        new_r = int(round(cur_r + recovered_frac * (def_r - cur_r)))
        new_g = int(round(cur_g + recovered_frac * (def_g - cur_g)))
        new_b = int(round(cur_b + recovered_frac * (def_b - cur_b)))

        self.color = f"#{new_r:02X}{new_g:02X}{new_b:02X}"
        return f"Après {time} minutes sans soleil, {self.name} a débronzé de {recovered_frac*100:.1f}% et a maintenant la couleur {self.color}."


    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'objet.
        """
        return f"Noe(name={self.name}, age={self.age}, profession={self.profession}, color={self.color})"
    
