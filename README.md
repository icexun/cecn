##经济日报电子版(paper.ce.cn) 爬虫程序

###使用scrapy编写的爬虫，主要是练手学习用，顺便帮某人统计查询自己的稿件

###运行步骤
开始前，要用crawl_days来指定从多少天前开始爬， 从而生成start_url. 然后从出版的报纸首页开始，先爬各板的link，之后再在各板块里获取每篇稿件，找到需要的记录。最后保存到mysql。
mysql中字段一次为id, pdate(出版日期)，author, title, subtitle, body(文章正文)

###爬完之后的查询一种方法
####比如要查署名为 谷夏 的所有稿件
SELECT * FROM cecn.paper where ((body like '%谷夏%') or (body like '%谷 夏%') or (author like '%谷夏%') or (author like '%谷 夏%') or (subtitle like '%谷夏%') or (subtitle like '%谷 夏%'));
