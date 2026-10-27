from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from pms_app.models import (
    User, TeamMember, Project, Task, Comment, Notification, PTeam,
)


# ─────────────────────────────────────────────
# User
# ─────────────────────────────────────────────
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ['email']
    list_display = ['id', 'u_name', 'email', 'role', 'is_active',
                    'is_verified', 'is_staff', 'is_deleted']
    list_filter = ['role', 'is_active', 'is_verified', 'is_staff', 'is_deleted']
    search_fields = ['u_name', 'email']
    readonly_fields = ['created_at', 'updated_at', 'last_login']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('u_name', 'role')}),
        ('Status', {'fields': ('is_active', 'is_verified', 'is_staff',
                               'is_superuser', 'is_deleted')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Timestamps', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('u_name', 'email', 'role', 'password1', 'password2',
                       'is_staff', 'is_active'),
        }),
    )


# ─────────────────────────────────────────────
# TeamMember
# ─────────────────────────────────────────────
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'role', 'experience',
                    'added_by', 'linked_user', 'is_deleted']
    list_filter = ['is_deleted', 'role']
    search_fields = ['name', 'email', 'skills', 'role']
    raw_id_fields = ['added_by', 'linked_user']
    readonly_fields = ['updated_at']


# ─────────────────────────────────────────────
# Project
# ─────────────────────────────────────────────
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['p_id', 'p_name', 'status', 'priority', 'created_by',
                    'deadline', 'created_at', 'is_deleted']
    list_filter = ['status', 'priority', 'is_deleted', 'created_at']
    search_fields = ['p_name', 'desc']
    filter_horizontal = ['supervisors']
    raw_id_fields = ['created_by']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'


# ─────────────────────────────────────────────
# Task
# ─────────────────────────────────────────────
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['t_id', 'title', 'status', 'priority', 'progress',
                    'p', 'assign_to', 'assign_by', 'due_date',
                    'is_deleted']
    list_filter = ['status', 'priority', 'is_deleted', 'p']
    search_fields = ['title', 'desc']
    raw_id_fields = ['p', 'assign_to', 'assign_by', 'created_by', 'parent']
    filter_horizontal = ['assignees']
    readonly_fields = ['created_at', 'update_last']
    list_select_related = ['p', 'assign_to']


# ─────────────────────────────────────────────
# Comment
# ─────────────────────────────────────────────
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['c_id', 't', 'u', 'priority', 'pin', 'created_at']
    list_filter = ['priority', 'pin', 'created_at']
    search_fields = ['desc']
    raw_id_fields = ['t', 'u']
    readonly_fields = ['created_at', 'updated_at']


# ─────────────────────────────────────────────
# Notification
# ─────────────────────────────────────────────
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['n_id', 'u', 'type', 'is_read', 'created_at',
                    'read_at', 'is_deleted']
    list_filter = ['type', 'is_read', 'created_at']
    search_fields = ['message', 'type']
    raw_id_fields = ['u']
    readonly_fields = ['created_at', 'read_at']


# ─────────────────────────────────────────────
# PTeam
# ─────────────────────────────────────────────
@admin.register(PTeam)
class PTeamAdmin(admin.ModelAdmin):
    list_display = ['pt_id', 'p', 't', 'tm']
    list_filter = ['p']
    search_fields = ['p__p_name', 't__title', 'tm__name']
    raw_id_fields = ['p', 't', 'tm']
    list_select_related = ['p', 't', 'tm']


# ─────────────────────────────────────────────
# Register custom User last
# ─────────────────────────────────────────────
admin.site.register(User, CustomUserAdmin)