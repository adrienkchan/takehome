from .encoders import AssetEncoder
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.db.utils import IntegrityError
from .models import Asset
import json

# Create your views here.

@require_http_methods(["GET", "POST"])
def asset_list(request):
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
def asset_show(request, pk):
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
                {"message": "Invalid Employee id"},
                status=404
            )
    elif request.method == "DELETE":
        count, _ = Asset.objects.get(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Asset.objects.get(id=pk).update(**content)
        asset = Asset.objects.get(id=pk)
        return JsonResponse(
            asset,
            encoder=AssetEncoder,
            safe=False,
        )
