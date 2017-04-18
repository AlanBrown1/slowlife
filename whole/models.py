from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
class Feedback(models.Model):
	STATUS_CHOICE = (
			('0', '未查看'),
			('1', '已查看'),
		)

	feedtime = models.DateTimeField('反馈时间', auto_now_add=True)
	feedpersonname = models.CharField('反馈人姓名', max_length=30, null=True, blank=True, default='佚名')
	feedpersonemail = models.EmailField('反馈人邮箱', null=True, blank=True)
	status = models.CharField('是否已查看', max_length=10, choices=STATUS_CHOICE)
	# feedcontent = UEditorField('反馈内容', height=600, width=1000,
 #        default=u'', blank=True, imagePath="feedback/content_images/",
 #        toolbars='besttome', filePath='feedback/content_files/')
	content = models.TextField('反馈内容', null=True, blank=True)