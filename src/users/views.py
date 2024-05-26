from django.shortcuts import render, redirect
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
from rest_framework import status
from django.urls import reverse
from django.contrib import messages
from quiz.models import Topic,Question,UserTopicScore
from django.shortcuts import redirect
from users.forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import requests
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum,Max
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, MinLengthValidator, RegexValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError as DRFValidationError

class Register(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        # Kiểm tra tính hợp lệ của email
        try:
            validate_email(email)
        except ValidationError:
            raise DRFValidationError({'email': 'Invalid email address'})

        # Kiểm tra tính hợp lệ của username
        if len(username) < 4:
            raise DRFValidationError({'username': 'Username must be at least 4 characters long'})
        username_validator = RegexValidator(regex='^[a-zA-Z0-9]+$', message='Username must contain only letters and numbers')
        try:
            username_validator(username)
        except ValidationError as e:
            raise DRFValidationError({'username': e.message})

        # Kiểm tra tính hợp lệ của password
        try:
            validate_password(password)
        except ValidationError as e:
            raise DRFValidationError({'password': e.messages})

        # Lưu user nếu tất cả các kiểm tra đều hợp lệ
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        messages.success(request, 'Account created successfully')
        return redirect(reverse('login_view'))


class loginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Thực hiện xác thực người dùng
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        login(request, user)
        # Kiểm tra nếu người dùng là admin
        if user.is_staff:
            # Nếu là admin, chuyển hướng đến trang homeadmin
            return redirect('home_admin')
        else:
            # Nếu không phải admin, chuyển hướng đến trang my_page
            return redirect('my_page')


       
    

class LogoutView(APIView):
    def post(self,request):
        logout(request)
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': ' logout success'
        }
        return render(request,'login.html')
class UserDetailView(APIView):
    def get(self,request,pk):
        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self,request,pk):   
        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Cập nhật dữ liệu người dùng từ các tham số truyền vào
        if 'username' in request.data:
            user.username = request.data['username']
        if 'email' in request.data:
            user.email = request.data['email']
        # Thêm các trường khác cần cập nhật nếu có

        # Lưu lại thay đổi
        user.save()

        # Tạo serializer với dữ liệu người dùng đã được cập nhật
        serializer = UserSerializer(user)

        return Response(serializer.data)


from django.shortcuts import render
from quiz.models import Topic, Question
@login_required
def user_info(request, pk):
    user = User.objects.filter(id=pk).first()  # Lấy thông tin người dùng dựa trên id
    if user is None:
        # Xử lý trường hợp không tìm thấy người dùng
        return render(request, 'user_not_found.html', {'message': 'User not found'})

    # Đếm số lượng topic mà người dùng đã tạo
    topic_count = Topic.objects.filter(user=user).count()

    # Đếm số lượng câu hỏi mà người dùng đã tạo
    question_count = Question.objects.filter(topic__user=user).count()

    # Truyền thông tin người dùng và các thông tin đã tính được vào template
    return render(request, 'user_info.html', {'user_data': user, 'topic_count': topic_count, 'question_count': question_count}) #, 'quiz_count': quiz_count
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

def home(request):
    return render(request, 'home.html')
def register_view(request):
    return render(request, 'register.html')
def home_content(request):
    return render(request, 'quiz.html')
def login_view(request):
    return render(request, 'login.html')

def info_page(request):
    return render(request, 'info.html')
def my_questions(request):
    # Lấy tất cả các câu hỏi của người dùng đang đăng nhập
    user_questions = Question.objects.filter(topic__user=request.user)
    user_topics = Topic.objects.filter(user=request.user)
    print(user_topics)
    return render(request, 'my_questions.html', {'user_topics': user_topics})

@login_required
def quiz_history(request):
    # Lấy danh sách quiz đã làm từ UserTopicScore model
    quizzes = UserTopicScore.objects.filter(user=request.user)
    return render(request, 'quiz_history.html', {'quizzes': quizzes})



class DeleteUser(APIView):
    def delete(self, request, pk):
        user = User.objects.filter(id=pk).first()
        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"success": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully')
            return redirect('home_admin')  # Chuyển hướng đến trang homeadmin
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})
def user_detail(request, pk):
    # Gọi REST API để lấy thông tin chi tiết của người dùng
    response = requests.get(f'http://127.0.0.1:8000/user/{pk}/')
    user_data = response.json()
    # Truyền dữ liệu vào template và render trang
    return render(request, 'user_detail.html', {'user_data': user_data})


def user_update_view(request, user_id):
    # Xử lý yêu cầu GET để hiển thị form cập nhật thông tin người dùng
    if request.method == 'GET':
        # Gửi yêu cầu REST API để lấy thông tin chi tiết của người dùng
        response = requests.get(f'http://127.0.0.1:8000/user/{user_id}/')
        if response.status_code == 200:
            user_data = response.json()
            return render(request, 'user_update.html', {'user_data': user_data})
        else:
            # Xử lý trường hợp không tìm thấy người dùng
            messages.error(request, 'User not found')
            return redirect('home_admin')
    # Xử lý yêu cầu POST để cập nhật thông tin người dùng
    elif request.method == 'POST':
        # Lấy dữ liệu từ form gửi lên
        updated_data = request.POST
        # Gửi yêu cầu REST API để cập nhật thông tin người dùng
        response = requests.put(f'http://127.0.0.1:8000/user/{user_id}/', data=updated_data)
        if response.status_code == 200:
            messages.success(request, 'User information updated successfully')
            return redirect('home_admin')
        else:
            # Xử lý trường hợp cập nhật thất bại
            messages.error(request, 'Failed to update user information')
            return redirect('home_admin')    

def search(request):
    query = request.GET.get('q')
    if query:
        topics = Topic.objects.filter(name__icontains=query)
        questions = Question.objects.filter(text__icontains=query)
    else:
        topics = Topic.objects.all()
        questions = Question.objects.all()
    
    context = {
        'topics': topics,
        'questions': questions,
        'query': query,
    }
    return render(request, 'search_results.html', context)
class HomeAdminView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        users = User.objects.all()
        return render(request, 'home_admin.html', {'users': users})
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #lấy ra tổng user và tổng topic tổng câu hỏi
        total_user = User.objects.all().count()
        total_topic = Topic.objects.all().count()
        total_questions = Question.objects.all().count()
        # lấy ra tổng số câu hỏi đã được trả lời
        total_answered_questions = UserTopicScore.objects.aggregate(total=Sum('total_questions_answered'))['total']
        # lấy ra tổng số câu hỏi sai
        total_incorrect_questions = UserTopicScore.objects.aggregate(total=Sum('incorrect_answers'))['total']
        # lấy ra tổng số câu hỏi đúng
        total_correct_questions = UserTopicScore.objects.aggregate(total=Sum('correct_answers'))['total']
        context['total_answered_questions'] = total_answered_questions
        context['total_correct_questions'] = total_correct_questions
        context['total_incorrect_questions'] = total_incorrect_questions
        context['total_user'] = total_user
        context['total_topic'] = total_topic
        context['total_questions'] = total_questions

        return context
class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'mypage.html'
    
    def get_context_data(self, **kwargs):
        # 
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        topics = Topic.objects.all()
        for topic in topics:
            topic.question_count = topic.questions.count()
            topic.created_by = topic.user.username
        for topic in topics:
            # lấy bản ghi mới nhất của người dùng trong chủ đề này
            latest_score = UserTopicScore.objects.filter(user = current_user,topic = topic).order_by('-created_at').first()
            if latest_score:
                # Tính toán phần trăm làm đúng
                percentage_correct = (latest_score.correct_answers / latest_score.total_questions_answered) * 100
                topic.percentage_correct = round(percentage_correct, 2)  # Làm tròn phần trăm đến 2 chữ số sau dấu thập phân
            else:
                topic.percentage_correct = None  # Nếu không có bản ghi nào, thiết lập phần trăm làm đúng là 0
        context['topics'] = topics
        context['current_user'] = current_user.username
        return context

