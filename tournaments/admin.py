from django.contrib import admin
from .models import Golfer, Tournament, Group, GroupGolfer, Member, MemberPick


admin.site.register(Golfer)
admin.site.register(Tournament)
admin.site.register(Group)
admin.site.register(GroupGolfer)
admin.site.register(Member)
admin.site.register(MemberPick)
