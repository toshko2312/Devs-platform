from django.shortcuts import render


class UsersCRUD:
    @staticmethod
    def get_multi(request):
        return render(request, 'users/profiles.html')