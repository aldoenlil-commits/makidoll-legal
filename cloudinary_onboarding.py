#!/usr/bin/env python3
"""Onboarding Cloudinary — flux complet en un seul fichier.

Lance ce script directement :  ./cloudinary_onboarding.py
(après avoir renseigné l'API secret ci-dessous).
"""

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import CloudinaryImage

# ---------------------------------------------------------------------------
# 1. Configuration de Cloudinary (bloc inline, pas de fichier .env)
# ---------------------------------------------------------------------------
cloudinary.config(
    cloud_name="dhxklbcx",            # Cloud name (réel)
    api_key="518929473176113",        # API key (réel)
    api_secret="YOUR_API_SECRET",     # ← replace this  (API secret à remplacer)
    secure=True,                      # force les URLs en HTTPS
)

# ---------------------------------------------------------------------------
# 2. Téléversement d'une image de démo (domaine res.cloudinary.com/demo/)
# ---------------------------------------------------------------------------
SAMPLE_IMAGE = "https://res.cloudinary.com/demo/image/upload/sample.jpg"

upload_result = cloudinary.uploader.upload(SAMPLE_IMAGE)

secure_url = upload_result["secure_url"]
public_id = upload_result["public_id"]

print("=== Téléversement ===")
print("Secure URL :", secure_url)
print("Public ID  :", public_id)

# ---------------------------------------------------------------------------
# 3. Récupération des métadonnées de l'image téléversée
# ---------------------------------------------------------------------------
details = cloudinary.api.resource(public_id)

print("\n=== Métadonnées ===")
print("Largeur (width)   :", details["width"], "px")
print("Hauteur (height)  :", details["height"], "px")
print("Format            :", details["format"])
print("Taille (bytes)    :", details["bytes"], "octets")

# ---------------------------------------------------------------------------
# 4. Transformation de l'image
#    - f_auto : Cloudinary choisit AUTOMATIQUEMENT le meilleur format
#               (WebP/AVIF…) selon le navigateur, pour un fichier plus léger.
#    - q_auto : Cloudinary ajuste AUTOMATIQUEMENT la qualité (compression)
#               sans perte visible, pour réduire encore le poids du fichier.
# ---------------------------------------------------------------------------
transformed_url = CloudinaryImage(public_id).build_url(
    fetch_format="auto",   # => f_auto
    quality="auto",        # => q_auto
)

print("\nDone! Click link below to see optimized version of the image. "
      "Check the size and the format.")
print("URL optimisée :", transformed_url)
