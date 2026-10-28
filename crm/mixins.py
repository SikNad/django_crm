from django.contrib.auth.mixins import UserPassesTestMixin

class RoleRequiredMixin(UserPassesTestMixin):
    allowed_roles = []

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return self.request.user.groups.filter(name__in=self.allowed_roles).exists()
