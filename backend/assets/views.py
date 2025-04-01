from .encoders import AssetEncoder
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest, JsonResponse
from django.db.utils import IntegrityError
from .models import Asset
import json

# Create your views here.

@require_http_methods(["GET", "POST"])
def asset_list(request: HttpRequest):
    if request.method == "GET":
        asset = Asset.objects.all()
        return JsonResponse(
            {"assets" : asset},
            encoder=AssetEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            asset = Asset.objects.create(**content)
        except IntegrityError:
            return JsonResponse(
                {"message": "Unable to create"},
                status=400
            )
        return JsonResponse(
            asset,
            encoder=AssetEncoder,
            safe=False,
        )

@require_http_methods(["GET", "DELETE", "PUT"])
def asset_show(request: HttpRequest, pk: int):
    if request.method == "GET":
        try:
            asset = Asset.objects.get(id=pk)
            return JsonResponse(
                asset,
                encoder=AssetEncoder,
                safe=False
            )
        except Asset.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Asset id"},
                status=404
            )
    elif request.method == "DELETE":
        try:
            count, _ = Asset.objects.get(id=pk).delete()
            return JsonResponse({"deleted": count > 0})
        except Asset.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Asset id"},
                status=404
            )
    else:
        content = json.loads(request.body)
        try:
            asset = Asset.objects.get(id=pk)
        except Asset.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Asset id"},
                status=404
            )
        for key, value in content.items():
            setattr(asset, key, value)
        asset.save()

        return JsonResponse(
            asset,
            encoder=AssetEncoder,
            safe=False,
        )
