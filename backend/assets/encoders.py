from common.encoders import ModelEncoder
from .models import Asset

class AssetEncoder(ModelEncoder):
    model = Asset
    properties = [
        "asset_name",
        "serial_number",
        "price",
        "color",
        "description",
        "cert_verification",
        "id",
    ]
