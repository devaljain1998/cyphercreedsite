from django.contrib import admin
from .models import Question, Answer, Comment
# Register your models here.

#Questions and Answers are needed to be modified
#admin.site.register(Question)
class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','user','content','created','is_active','tag_list') 
    fields = ('title','user','content','is_active','tags')
    inlines = [AnswerInline]
    list_filter = ('created','is_active','user','tags')
    search_fields = ('title','content',) #tags cannot be searched

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in Question.tags.all())

#admin.site.register(Answer)
class CommentInline(admin.TabularInline):
    model = Comment
# class QuestionInline(admin.TabularInline):
#     model = Question

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','user','content','created','upvotes','is_active') 
    fields = ('title',('user','content'),('upvotes','is_active'))
    inlines = [CommentInline]
    list_filter = ('created','is_active','user','upvotes','question')
    search_fields = ('content',) #tags cannot be searched

admin.site.register(Comment)
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('content','created','answer') #'user'
#     fields = ('answer','content','created')
