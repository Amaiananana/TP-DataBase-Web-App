from django.shortcuts import render, redirect
from .models import UserProfile

from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user_profiles(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)

def home(request):
    error = ''

    if request.method == 'POST':
        fname = request.POST.get('fname', '').strip()
        mname = request.POST.get('mname', '').strip()
        lname = request.POST.get('lname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        gender = request.POST.get('gender', '').strip()
        dob = request.POST.get('dob', '').strip()
        course = request.POST.get('course', '').strip()

        # Validate required fields
        if not all([fname, lname, email, password, gender, dob, course]):
            error = "Please fill in all required fields."
        elif UserProfile.objects.filter(email=email).exists():
            error = "This email is already registered. Please use a different email."
        else:
            # Create and save user
            user = UserProfile.objects.create(
                fname=fname,
                mname=mname,
                lname=lname,
                email=email,
                password=password,
                gender=gender,
                dob=dob,
                course=course
            )
            # Store email in session
            request.session['user_email'] = user.email
            return redirect('profile')

    return render(request, 'home.html', {'error': error})


def profile(request):
    user_email = request.session.get('user_email')

    if not user_email:
        return render(request, 'profile.html', {'error': 'Session expired or user not registered'})

    user = UserProfile.objects.filter(email=user_email).first()

    if not user:
        return render(request, 'profile.html', {'error': 'User not found'})

    return render(request, 'profile.html', {'user': user})
