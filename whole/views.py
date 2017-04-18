from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse  # 用于逆向获取网址
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 用于分页
from .deHTML import _DeHTMLParser  # 用户将HTML文本转为纯文本

from life.models import Life        # 导入life模块的Life表
from music.models import Music      # 导入music模块的Music表
from travel.models import Travel    # 导入travel模块的Travel表    
from lit.models import Lit          # 导入lit模块的Lit表
from whole.models import Feedback   # 导入意见反馈表
from .forms import ImageUploadForm, FileUploadForm # 从form.py中引入表单
# Create your views here.

# 返回首页 *******************************************************************
def home(request):
	# 慢生活模块
	# 获取子类(美食food)最新一篇文章
	food = Life.objects.filter(tag=0).order_by('-publishtime')[0] 
	creation = Life.objects.filter(tag=1).order_by('-publishtime')[0]
	pet = Life.objects.filter(tag=2).order_by('-publishtime')[0]
	health = Life.objects.filter(tag=3).order_by('-publishtime')[0]
	emotion = Life.objects.filter(tag=4).order_by('-publishtime')[0]
	flower = Life.objects.filter(tag=5).order_by('-publishtime')[0]

	# 慢音乐模块
	# 获取子类（推荐recommend）最新一篇文章
	recommend1 = Music.objects.filter(tag=0).order_by('-publishtime')[0]
	recommend2 = Music.objects.filter(tag=0).order_by('-publishtime')[1]
	singer = Music.objects.filter(tag=1).order_by('-publishtime')[0]
	album = Music.objects.filter(tag=2).order_by('-publishtime')[0]
	category = Music.objects.filter(tag=3).order_by('-publishtime')[0]
	mood = Music.objects.filter(tag=4).order_by('-publishtime')[0]

	# 慢旅行模块
	# 获取子类（推荐recommend）最新一篇文章
	photography = Travel.objects.filter(tag=0).order_by('-publishtime')[0]
	scene = Travel.objects.filter(tag=1).order_by('-publishtime')[0]
	record = Travel.objects.filter(tag=2).order_by('-publishtime')[0]
	strategy = Travel.objects.filter(tag=3).order_by('-publishtime')[0]
	hotel = Travel.objects.filter(tag=4).order_by('-publishtime')[0]

	# 慢文学模块 
	famous1 = Lit.objects.filter(tag=0).order_by('-publishtime')[0]
	famous2 = Lit.objects.filter(tag=0).order_by('-publishtime')[1]
	fineart1 = Lit.objects.filter(tag=1).order_by('-publishtime')[0]
	fineart2 = Lit.objects.filter(tag=1).order_by('-publishtime')[1]
	fineart3 = Lit.objects.filter(tag=1).order_by('-publishtime')[2]
	poem1 = Lit.objects.filter(tag=2).order_by('-publishtime')[0]
	poem2 = Lit.objects.filter(tag=2).order_by('-publishtime')[1]
	pillowbook1 = Lit.objects.filter(tag=3).order_by('-publishtime')[0]
	pillowbook2 = Lit.objects.filter(tag=3).order_by('-publishtime')[1]
	essay1 = Lit.objects.filter(tag=4).order_by('-publishtime')[0]
	essay2 = Lit.objects.filter(tag=4).order_by('-publishtime')[1]
	essay3 = Lit.objects.filter(tag=4).order_by('-publishtime')[2]

	# 慢推荐模块
	fa_life1 = Life.objects.filter(tag=4).order_by('-zan')[0] # 生活情感类赞最多的
	fa_life2 = Life.objects.filter(tag=5).order_by('-zan')[0] # 生活花草类赞最多的
	fa_music = Music.objects.filter(tag=0).order_by('-zan')[0] # 音乐推荐类赞最多
	fa_travel = Travel.objects.filter(tag=1).order_by('-zan')[0] # 旅行景点类赞最多
	fa_lit = Lit.objects.filter(tag=1).order_by('zan')[0] #文学美文类赞最多的

	# 把文章合起来，准备传送到前端
	content = { 'life': {'food': food, 'creation': creation, 'pet': pet, 
						'health': health, 'emotion': emotion, 'flower':flower},
				'music':{'recommend1':recommend1, 'recommend2':recommend2, 
						'singer':singer, 'album':album,	'category':category, 'mood':mood},
				'travel':{'photography':photography, 'scene':scene, 'record':record, 
						'strategy':strategy, 'hotel':hotel},
				'lit':{ 'famous1':famous1, 'famous2':famous2, 'fineart1':fineart1,
						'fineart2':fineart2,'fineart3':fineart3, 'poem1':poem1,
						'poem2':poem2, 'pillowbook1':pillowbook1, 'pillowbook2':pillowbook2,
						'essay1':essay1, 'essay2':essay2, 'essay3':essay3},
				'fa': {'fa_life1':fa_life1, 'fa_life2':fa_life2, 'fa_music':fa_music,
						'fa_travel':fa_travel, 'fa_lit':fa_lit},
			}

	# 这里把记录的content截取一部分来显示，而不是显示全部
	for k1 in content:
		temp1 = content[k1]
		for k2 in temp1:
			temp2 = temp1[k2]
			temp2.content = dehtml(temp2.content)
			if len(temp2.content) > 50:
				temp2.content = temp2.content.replace(' ','')
				temp2.content = temp2.content[0:50]

	return render(request, 'base_home.html', content)

def dehtml(text):  
    try:  
        parser = _DeHTMLParser()  
        parser.feed(text)  
        parser.close()  
        return parser.text()  
    except:  
        print_exc(file=stderr)  
        return text  


# 获取最新文章（6篇）和慢生活精选文章（6篇）
def get_new():
	# 最新文章，选时间最近的
	new_life = Life.objects.order_by('-publishtime')[0:2]
	new_music = Music.objects.order_by('-publishtime')[0]
	new_travel = Travel.objects.order_by('-publishtime')[0]
	new_lit = Lit.objects.order_by('-publishtime')[0:2]

	# 慢生活精选，选赞最多的
	jing_life = Life.objects.order_by('-zan')[0:2]
	jing_music = Music.objects.order_by('-zan')[0]
	jing_travel = Travel.objects.order_by('-zan')[0]
	jing_lit = Lit.objects.order_by('-zan')[0:2]

	return (new_life, new_music, new_travel, new_lit,
			jing_life, jing_music, jing_travel, jing_lit)


# 返回主导航栏对应的页面 ******************************************************
# 这个函数用来从数据库中取出相应数据，顺序从新到旧
def getMainData(navname):   
	articles = None;
	if navname=='life':
		if Life.objects.all().exists(): # 如果有数据的话
			articles = Life.objects.order_by('-publishtime')
	elif navname=='music':
		if Music.objects.all().exists():
			articles = Music.objects.order_by('-publishtime')
	elif navname=='travel':
		if Travel.objects.all().exists():
			articles = Travel.objects.order_by('-publishtime')
	elif navname=='lit':
		if Lit.objects.all().exists():
			articles = Lit.objects.order_by('-publishtime')

	return articles

def mainpage(request, navname, page_now): # navname是大类：life/music/travel/lit
	articles = getMainData(navname)
	(new_life, new_music, new_travel, new_lit, 
		jing_life, jing_music, jing_travel, jing_lit) = get_new()
	# page_now是“p1”，即p后面加上数据的形式，因此需要取出数字
	page_now = int(page_now[1 : len(page_now)])

	if articles != None:  # 如果从数据库中获取到了数据的话
		p = Paginator(articles, 10)  # 每页展示10篇文章
		try:
			articles_now = p.page(page_now)  # 获取第page_now页的数据
			for i in range(len(articles_now)):
				articles_now[i].content = dehtml(articles_now[i].content)
				articles_now[i].content = articles_now[i].content.replace(' ','')
				articles_now[i].content = articles_now[i].content[0:150]
		except PageNotAnInteger:   # 如果页码不是整数，就返回第一页数据
			articles_now = p.page(1)
		except EmptyPage:          # 如果页码不存在，就返回最后一页数据
			articles_now = p.page(p.num_pages)

		pages_count = p.num_pages  # 总页数
		content = { 'navname': navname,
					'pages_count': json.dumps(pages_count),
					'page_now': page_now,
					'articles': articles_now ,
					'new_life': new_life,
					'new_music': new_music,
					'new_travel': new_travel,
					'new_lit': new_lit,
					'jing_life': jing_life,
					'jing_music': jing_music,
					'jing_travel': jing_travel,
					'jing_lit': jing_lit,
				}
		# 返回主导航栏页面
		return render(request, 'base_main_page.html', content)
	else:
		# 返回404页面
		return render(request, 'notfoundpage.html')

# 返回次导航栏对应的页面 *****************************************************
# 这个函数用来从数据库中取出相应数据，从新到旧
def getSubData(navname):
	articles = None;
	life_class = ['food', 'creation', 'pet', 'health', 'emotion', 'flower']
	music_class = ['recommend', 'singer', 'album', 'category', 'mood']
	travel_class = ['photography', 'scene', 'record', 'strategy', 'hotel']
	lit_class = ['famous', 'fineart', 'poem', 'pillowbook', 'essay']
	articles = None
	if navname in life_class:
		fenlei = 'life'
		ind = life_class.index(navname)
		articles = Life.objects.filter(tag=str(ind)).order_by('-publishtime')
	elif navname in music_class:
		fenlei = 'music'
		ind = music_class.index(navname)
		articles = Music.objects.filter(tag=str(ind)).order_by('-publishtime')
	elif navname in travel_class:
		fenlei = 'travel'
		ind = travel_class.index(navname)
		articles = Travel.objects.filter(tag=str(ind)).order_by('-publishtime')
	elif navname in lit_class:
		fenlei = 'lit'
		ind = lit_class.index(navname)
		articles = Lit.objects.filter(tag=str(ind)).order_by('-publishtime')
	return (fenlei, articles)


def subpage(request, navname, page_now):
	(fenlei, articles) = getSubData(navname)
	(new_life, new_music, new_travel, new_lit, 
		jing_life, jing_music, jing_travel, jing_lit) = get_new()
	# page_now是“p1”，即p后面加上数据的形式，因此需要取出数字
	page_now = int(page_now[1 : len(page_now)])

	if articles != None:  # 如果从数据库中获取到了数据的话
		p = Paginator(articles, 10)  # 每页展示10篇文章
		try:
			articles_now = p.page(page_now)  # 获取第page_now页的数据
			for i in range(len(articles_now)):
				articles_now[i].content = dehtml(articles_now[i].content)
				articles_now[i].content = articles_now[i].content.replace(' ','')
				articles_now[i].content = articles_now[i].content[0:150]
		except PageNotAnInteger:   # 如果页码不是整数，就返回第一页数据
			articles_now = p.page(1)
		except EmptyPage:          # 如果页码不存在，就返回最后一页数据
			articles_now = p.page(p.num_pages)

		pages_count = p.num_pages  # 总页数
		content = { 'navname': navname,
					'fenlei': fenlei,
					'pages_count': json.dumps(pages_count),
					'page_now': page_now,
					'articles': articles_now ,
					'new_life': new_life,
					'new_music': new_music,
					'new_travel': new_travel,
					'new_lit': new_lit,
					'jing_life': jing_life,
					'jing_music': jing_music,
					'jing_travel': jing_travel,
					'jing_lit': jing_lit,
				}
		# 返回主导航栏页面
		return render(request, 'base_sub_page.html', content)
	else:
		# 返回404页面
		return render(request, 'notfoundpage.html')


# 分页 ********************************************************************
def getMainPage(request):  # 前端通过ajax请求需要转跳的目标网址
	navname = request.GET['navname']
	page_now = request.GET['page_now']
	# 使用reverse逆向获取网址
	page_url = reverse('mainpage', args=(navname, page_now))
	return HttpResponse(page_url)

def getSubPage(request):
	navname = request.GET['navname']
	page_now = request.GET['page_now']
	page_url = reverse('subpage', args=(navname, page_now))
	return HttpResponse(page_url)

# 返回文章页面 **************************************************************
def article(request, fenlei, id):
	(new_life, new_music, new_travel, new_lit, 
		jing_life, jing_music, jing_travel, jing_lit) = get_new()

	if fenlei=='life':
		article = Life.objects.get(id=id)
	elif fenlei=='music':
		article = Music.objects.get(id=id)
	elif fenlei=='travel':
		article = Travel.objects.get(id=id)
	elif fenlei=='lit':
		article = Lit.objects.get(id=id)

	content = { 'fenlei': fenlei,
				'article': article,
				'new_life': new_life,
				'new_music': new_music,
				'new_travel': new_travel,
				'new_lit': new_lit,
				'jing_life': jing_life,
				'jing_music': jing_music,
				'jing_travel': jing_travel,
				'jing_lit': jing_lit,
			}
	return render(request, 'base_article.html', content)
	

# 返回“关于我们”页面 ******************************************************
def aboutus(request, position):
	(new_life, new_music, new_travel, new_lit, 
		jing_life, jing_music, jing_travel, jing_lit) = get_new()

	pos = position
	if pos == 'head':
		return render(request, 'base_aboutus.html')
	else:
		content = { 'pos': json.dumps(pos),
					'new_life': new_life,
					'new_music': new_music,
					'new_travel': new_travel,
					'new_lit': new_lit,
					'jing_life': jing_life,
					'jing_music': jing_music,
					'jing_travel': jing_travel,
					'jing_lit': jing_lit,
				}
		return render(request, 'base_aboutus.html', content)

# 返回慢推荐页面 **********************************************************
# life、music、travel、lit模块各选择两个赞最高的
def manrecommend(request):
	man_life1 = Life.objects.order_by('-zan')[0]
	man_life2 = Life.objects.order_by('-zan')[1]
	man_music1 = Music.objects.order_by('-zan')[0]
	man_music2 = Music.objects.order_by('-zan')[1]
	man_travel1 = Travel.objects.order_by('-zan')[0]
	man_travel2 = Travel.objects.order_by('-zan')[1]
	man_lit1 = Lit.objects.order_by('-zan')[0]
	man_lit2 = Lit.objects.order_by('-zan')[1]
	content = { 'man_life1':man_life1, 'man_life2':man_life2,
				'man_music1':man_music1, 'man_music2':man_music2,
				'man_travel1':man_travel1,'man_travel2':man_travel2,
				'man_lit1':man_lit1, 'man_lit2':man_lit2,
				}
	for k in content:
		temp = content[k]
		temp.content = dehtml(temp.content)
		if len(temp.content) > 150:
			temp.content = temp.content[0:150]
	return render(request, 'base_man_recommend.html', content)

# 给文章点赞 *************************************************************
# 前端使用ajax向后台发送了get请求
def zan(request):
	fenlei = request.GET['fenlei']
	id = request.GET['id']
	if fenlei=='life':
		article = Life.objects.get(id=id)
	elif fenlei=='music':
		article = Music.objects.get(id=id)
	elif fenlei=='travel':
		article = Travel.objects.get(id=id)
	elif fenlei=='lit':
		article = Lit.objects.get(id=id)

	if article.zan < 99:
		article.zan = article.zan + 1
		zan_num = str(article.zan)
	else:  # 如果点赞数>=99，就显示99+且数据库内点赞数不再累加
		article.zan = 99 # 如果数据库内文章的赞数本来就>=99，则置为99
		zan_num = '99+'
	article.save()
	# 返回赞了之后的赞数
	return HttpResponse(zan_num)

# 处理意见反馈 *************************************************************
def advise(request):  
	if request.method == 'POST':
		try:
			content = request.POST['content']
			fileType = request.POST['fileType']
			Feedback.objects.get_or_create(
					status = '0',
					content = content,
				)
			return HttpResponse('ok')
		except:
			return HttpResponse('wrong')

# 返回404页面
# def page_not_found(request):
#         return render_to_response("notfoundpage.html")