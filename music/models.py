from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Music(models.Model):
	TAG_CHOICE = (
			('0', '推荐'),
			('1', '歌手'),
			('2', '专辑'),
			('3', '类型'),
			('4', '心情'),
		)
	STATUS_CHOICE = (
			('0', '未审核'),
			('1', '已审核'),
		)

	title = models.CharField('标题', max_length=128)
	author = models.CharField('作者', max_length=30)
	publishtime = models.DateTimeField('发布日期', auto_now_add=True)
	updatetime = models.DateTimeField('更新日期', auto_now=True)
	tag = models.CharField('标签', max_length=30, choices=TAG_CHOICE)
	status = models.CharField('是否审核', max_length=20, choices=STATUS_CHOICE)
	zan = models.IntegerField('赞', default=0)
	image = models.ImageField('封面', upload_to='music/images', null=True, blank=True
								, help_text='图像尺寸：130*170')
	audio = models.FileField('音频', upload_to='music/audios', null=True, blank=True)
	content = UEditorField('内容', height=600, width=1000,
				        default='', blank=True, imagePath="music_content/images/",
				        toolbars='besttome', filePath='music_content/files/')

	def __str__(self):
		return self.title