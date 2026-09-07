import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import InviteeForm
from .models import Invitee


@login_required
def invitees_list(request):
    """Render the primary invitees dashboard with live counts and filtering."""
    invitees_qs = Invitee.objects.all()

    # Query metrics & aggregations
    total_invitees = invitees_qs.count()
    total_guests = invitees_qs.aggregate(total=Sum("guest_count"))["total"] or 0

    alex_invitees = invitees_qs.filter(side=Invitee.SIDE_ALEX).count()
    alex_guests = invitees_qs.filter(side=Invitee.SIDE_ALEX).aggregate(total=Sum("guest_count"))["total"] or 0

    divya_invitees = invitees_qs.filter(side=Invitee.SIDE_DIVYA).count()
    divya_guests = invitees_qs.filter(side=Invitee.SIDE_DIVYA).aggregate(total=Sum("guest_count"))["total"] or 0

    # Relationship counts
    relationships_data = []
    for rel_code, rel_label in Invitee.RELATIONSHIP_CHOICES:
        rel_qs = invitees_qs.filter(relationship=rel_code)
        cnt = rel_qs.count()
        g_cnt = rel_qs.aggregate(total=Sum("guest_count"))["total"] or 0
        relationships_data.append({
            "code": rel_code,
            "label": rel_label,
            "count": cnt,
            "guests": g_cnt,
        })

    form = InviteeForm()

    # If JSON requested via fetch
    if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.GET.get("format") == "json":
        data = [inv.to_dict() for inv in invitees_qs]
        return JsonResponse({
            "invitees": data,
            "metrics": {
                "total_invitees": total_invitees,
                "total_guests": total_guests,
                "alex_invitees": alex_invitees,
                "alex_guests": alex_guests,
                "divya_invitees": divya_invitees,
                "divya_guests": divya_guests,
                "relationships": {r["code"]: {"count": r["count"], "guests": r["guests"]} for r in relationships_data},
            }
        })

    context = {
        "active_tab": "invitees",
        "invitees": invitees_qs,
        "total_invitees": total_invitees,
        "total_guests": total_guests,
        "alex_invitees": alex_invitees,
        "alex_guests": alex_guests,
        "divya_invitees": divya_invitees,
        "divya_guests": divya_guests,
        "relationships_data": relationships_data,
        "form": form,
    }
    return render(request, "planner/invitees.html", context)


@login_required
@require_http_methods(["POST"])
def invitee_create(request):
    """Create a new invitee."""
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.content_type == "application/json"
    
    if request.content_type == "application/json":
        try:
            body = json.loads(request.body)
            form = InviteeForm(body)
        except Exception:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
    else:
        form = InviteeForm(request.POST)

    if form.is_valid():
        invitee = form.save()
        if is_ajax:
            return JsonResponse({
                "status": "success",
                "message": f"Successfully added {invitee.name}!",
                "invitee": invitee.to_dict(),
            })
        messages.success(request, f"Successfully added {invitee.name}!")
        return redirect("invitees_list")
    else:
        if is_ajax:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
        messages.error(request, "Please correct the errors in the form.")
        return redirect("invitees_list")


@login_required
@require_http_methods(["GET", "POST"])
def invitee_update(request, pk):
    """Get invitee details or update an existing invitee."""
    invitee = get_object_or_404(Invitee, pk=pk)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.content_type == "application/json"

    if request.method == "GET":
        return JsonResponse({"status": "success", "invitee": invitee.to_dict()})

    if request.content_type == "application/json":
        try:
            body = json.loads(request.body)
            form = InviteeForm(body, instance=invitee)
        except Exception:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
    else:
        form = InviteeForm(request.POST, instance=invitee)

    if form.is_valid():
        invitee = form.save()
        if is_ajax:
            return JsonResponse({
                "status": "success",
                "message": f"Successfully updated {invitee.name}!",
                "invitee": invitee.to_dict(),
            })
        messages.success(request, f"Successfully updated {invitee.name}!")
        return redirect("invitees_list")
    else:
        if is_ajax:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
        messages.error(request, "Please correct the errors in the form.")
        return redirect("invitees_list")


@login_required
@require_http_methods(["POST"])
def invitee_delete(request, pk):
    """Delete an invitee."""
    invitee = get_object_or_404(Invitee, pk=pk)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    name = invitee.name
    invitee.delete()

    if is_ajax:
        return JsonResponse({
            "status": "success",
            "message": f"Successfully deleted {name}.",
            "id": pk,
        })
    messages.success(request, f"Deleted {name}.")
    return redirect("invitees_list")


@login_required
def budget_view(request):
    """Render the Budget overview page with expense categories and tracker."""
    context = {
        "active_tab": "budget",
        "estimated_total": 45000,
        "actual_total": 38500,
        "paid_total": 24200,
        "categories": [
            {
                "name": "Venues & Reception",
                "icon": "building",
                "estimated": 15000,
                "actual": 14500,
                "paid": 10000,
                "notes": "La Mirage Convention Center & Church fees",
            },
            {
                "name": "Catering & Banquet",
                "icon": "utensils",
                "estimated": 12000,
                "actual": 11000,
                "paid": 6000,
                "notes": "Engagement lunch & wedding banquet menus",
            },
            {
                "name": "Photography & Videography",
                "icon": "camera",
                "estimated": 6000,
                "actual": 5500,
                "paid": 4000,
                "notes": "Full day coverage, drones & albums",
            },
            {
                "name": "Attire & Beauty",
                "icon": "shirt",
                "estimated": 5000,
                "actual": 4200,
                "paid": 3000,
                "notes": "Bridal gowns, suits, makeup & styling",
            },
            {
                "name": "Decor & Floral",
                "icon": "sparkles",
                "estimated": 4500,
                "actual": 4000,
                "paid": 2000,
                "notes": "Stage backdrop, aisle florals & centerpieces",
            },
            {
                "name": "Music & Entertainment",
                "icon": "music",
                "estimated": 2500,
                "actual": 2300,
                "paid": 1200,
                "notes": "Live acoustic band & DJ sound system",
            },
        ],
    }
    return render(request, "planner/budget.html", context)
