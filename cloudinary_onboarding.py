#!/usr/bin/env python3
"""Onboarding Cloudinary — flux complet en un seul fichier (équivalent Python
du Quick Start officiel `index.js`).

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
    api_secret="YOUR_API_SECRET",     # ← replace this  (Click 'View API Keys' pour copier le secret)
    secure=True,                      # force les URLs en HTTPS
)

# ---------------------------------------------------------------------------
# 2. Téléversement d'une image de démo (domaine res.cloudinary.com/demo/)
#    Mêmes valeurs que le Quick Start officiel : image "shoes", public_id "shoes".
# ---------------------------------------------------------------------------
SAMPLE_IMAGE = "https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg"

upload_result = cloudinary.uploader.upload(SAMPLE_IMAGE, public_id="shoes")

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
# 4. Transformations de l'image
# ---------------------------------------------------------------------------

# URL optimisée :
#   - f_auto : Cloudinary choisit AUTOMATIQUEMENT le meilleur format
#              (WebP/AVIF…) selon le navigateur, pour un fichier plus léger.
#   - q_auto : Cloudinary ajuste AUTOMATIQUEMENT la qualité (compression)
#              sans perte visible, pour réduire encore le poids du fichier.
optimize_url = CloudinaryImage("shoes").build_url(
    fetch_format="auto",   # => f_auto
    quality="auto",        # => q_auto
)

# URL transformée (recadrage carré) :
#   - c_auto (crop="auto") : recadrage automatique intelligent.
#   - g_auto (gravity="auto") : centre le cadrage sur le sujet le plus pertinent.
#   - width/height 500 : génère une variante 500x500 du même original.
auto_crop_url = CloudinaryImage("shoes").build_url(
    crop="auto",
    gravity="auto",
    width=500,
    height=500,
)

print("\nDone! Click link below to see optimized version of the image. "
      "Check the size and the format.")
print("URL optimisée (f_auto/q_auto) :", optimize_url)
print("URL recadrée  (auto 500x500)  :", auto_crop_url)
